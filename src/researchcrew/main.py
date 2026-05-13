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
    core_task = ''
    context = ''
    current_feedback = ''
    input_dir = Path(os.environ['INPUT_DIR'])
    output_dir = Path(os.environ['OUTPUT_DIR'])
    input_file = input_dir / "input.md"
    with open(input_file, 'r') as f:
        core_task = f.read()
    
    # get the context
    files=sorted(output_dir.glob("*.md"))
    if len(files) > 0:
        last_feedback_file = files[-1]
        with open(last_feedback_file, 'r') as f:
            current_feedback += f.read()
            if '## User feedback' not in current_feedback:
                print("no user feedback on the previous result")
                exit()

        for file in files[:-1]:
            context += f'<context>Research from {file.name}</context>'
            with open(files[-1], 'r') as f:
                context += f.read()

    print(f"Research starting on the topic: \n {core_task}")
    inputs = {
        'core_task': core_task,
        'context': context,
        'current_feedback': current_feedback,
        'current_year': str(datetime.now().year),
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
