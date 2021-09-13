"""

Notes:
- _intentYN_: was the intent behind the statement to offend
- _sexYN_: is the post a sexual or lewd reference
- _offensiveYN_: could the post be offensive to anyone

Task 201:
Is this phrase intentionally offensive? Binary classification.

"""
import pandas as pd
import json

# Read in data
df = pd.read_csv("SBIC.v2.trn.csv")

# Save filename
save_filename = 'task201_sbic_intentional_offense_binary_classification.json'

task = dict()

task['Contributors'] = ["Arlen Fan"]
task['Source'] = ["SBIC"]
task['Categories'] = ["Binary Classification"]
task['Definition'] = "You will be provided with a text input. Your task is to deduce if the post is " \
                     "intentionally offensive. Please closely consider offensive statements that appear to " \
                     "be unintentional, or non-offensive statements that are underhandedly offensive. " \
                     "Your answer is a simple yes/no or True/False response, indicating if you believe a " \
                     "sentence/paragraph is intentionally offensive."

task['Positive Examples'] = [
    {"input": "", "output": "", "explanation": ""},
    {"input": "", "output": "", "explanation": ""},
]

task['Negative Examples'] = [
    {"input": "", "output": "", "explanation": ""},
    {"input": "", "output": "", "explanation": ""},
]

"""
100-6500 instances
"""
