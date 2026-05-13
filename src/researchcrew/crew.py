import os
from datetime import datetime
from pathlib import Path
from typing import Tuple, Any
from crewai import (
    Agent,
    Crew,
    Process,
    Task,
    TaskOutput,
    LLM
)
from crewai.project import (
    CrewBase,
    agent,
    crew,
    task
)
from crewai.agents.agent_builder.base_agent import BaseAgent

from researchcrew.tools.ai_tools import exa_tool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

def validate_report_content(result: TaskOutput) -> Tuple[bool, Any]:
    # check if the report has the keywords summary, etc
    report_str = result.raw
    keywords_to_check = ['# Summary of the task',
                         '# Clarifying questions to the user (if any)',
                         '# Possible future direction of investigation (if any)']
    if all(keyword in report_str for keyword in keywords_to_check):
        return (True, 'Final report contains all necessary keywords')
    else:
        return (False, 'Final report does not contain all necessary keywords')

def get_next_report_path() -> str:
    output_dir = Path(os.environ['OUTPUT_DIR'])
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    next_report_path = output_dir / f"{year}{int(month):02d}{int(day):02d}.md"
    return str(next_report_path)

@CrewBase
class Researchcrew():
    """Researchcrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def research_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['research_planner'], # type: ignore[index]
            verbose=True,
            max_retry_limit=2,
        )

    @agent
    def web_crawler(self) -> Agent:
        return Agent(
            config=self.agents_config['web_crawler'], # type: ignore[index]
            tools=[exa_tool],
            verbose=True,
            max_retry_limit=2,
        )

    @agent
    def webscraper(self) -> Agent:
        return Agent(
            config=self.agents_config['webscraper'], # type: ignore[index]
            tools=[exa_tool],
            verbose=True,
            max_retry_limit=2,
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def reserach_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_planner_task'], # type: ignore[index]
        )

    @task
    def webcrawler_task(self) -> Task:
        return Task(
            config=self.tasks_config['webcrawler_task'], # type: ignore[index]
        )
    
    @task
    def webscraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['webscraper_task'], # type: ignore[index]
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file=get_next_report_path(),
            guardrail=validate_report_content
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Researchcrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            embedder={
                "provider": "google-generativeai",
                "config": {
                    "model": "gemini-embedding-001",
                    }
                    },
            memory=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
