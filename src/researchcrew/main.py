#!/usr/bin/env python
import os
from pathlib import Path
import sys
import warnings
from dotenv import load_dotenv
from datetime import datetime
from researchcrew.crew import Researchcrew
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    input_dir = Path(os.environ['INPUT_DIR'])
    output_dir = Path(os.environ['OUTPUT_DIR'])
    # list and sort files
    files=sorted(output_dir.glob("*.md"))
    if len(files) > 0:
        with open(files[-1], 'r') as f:
            topic = f.read()
        # check if user feedback exists in the file
        if '## User feedback' not in topic:
            print("no user feedback on the previous result")
            exit()
    else:
        input_file = input_dir / "input.md"
        with open(input_file, 'r') as f:
            topic = f.read()
    print(f"Research starting on the topic: \n {topic}")
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year),
        'industry_type': "Food industry",
    }

    try:
        Researchcrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Most popular food products on the German supermarket shelves and their nutritional values",
        'current_year': str(datetime.now().year)
    }
    try:
        Researchcrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Researchcrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        Researchcrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = Researchcrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
