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
