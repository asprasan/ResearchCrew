# Researchcrew Crew

Welcome to the Researchcrew project, powered by [crewAI](https://crewai.com). 

The goal of this project is to provide a multi-agent system that can perform complex research tasks, leveraging the capabilities of various AI agents working together, with a human in the loop that guides the process.


## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Setting up Environment Variables

The crew and the agents need an LLM to operate. You can use any LLM supported by crewAI. 

As of now, we use a single LLM for all the tasks. In the future, we may choose to use different LLMs for tasks of different complexity.

```bash
cp .env.example .env
```

Then, edit the `.env` file and add your API keys.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the ResearchCrew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Crew workflow

This crew is designed to perform research tasks. The workflow is as follows:

1. The crew receives a research question or topic to investigate.
2. The crew itself consists of an agentic flow. The flow is directed as follows:
   - The first task is a web-crawler task that searches the web for relevant information on the topic
   - The next task is to scrape the content of the links found by the web-crawler
   - Then, a research assistant agent reads the scraped content and extracts the relevant information
   - Finally, a report writer agent takes the extracted information and writes a report in markdown format.
3. A final report is generated and saved as `report.md` in the root folder.
4. The user then reviews the report and can provide feedback to the crew for further refinement or additional research.
5. Based on the feedback, the crew can iterate on the research process, refining the report or exploring additional sources as needed.

## Design choices

The defining feature of this crew is that there is a human in the loop that guides the research process. The research isn't complete within a single run of the crew. Instead, the crew produces a report that is then reviewed by the user, who can provide feedback for further refinement. This iterative process allows for a more thorough and accurate research outcome.

### Research crew needs to remember the core task and the research completed so far

User provides feedback after each run. However, the crew needs to remember the core task and the research completed so far in order to effectively incorporate the user's feedback and continue refining the report.

- Option 1: Set `memory=True` for the Crew. CrewAI stores long-term memory into a SQLite database. This long-term memory consists of the past outputs and can be queried when running subsequent iterations of the Crew
  - Feasibility: This is feasible as we let CrewAI decide what to remember. It can also cache some of the webpages crawled and scraped by the EXASearch tool.
- Option 2: Read all the previously generated reports and the input core-task provided by the user provide it as a context to the Crew.
  - Feasibility: Since the reports generated and the input task are all formatted as markdown, we can quite easily provide the raw information as context. This doesn't exceed the context limit of the LLMs which are usually around 250k - 1M tokens.

### Links need to be properly attributed in the final report
