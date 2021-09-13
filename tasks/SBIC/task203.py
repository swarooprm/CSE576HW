"""

Notes:
- _intentYN_: was the intent behind the statement to offend
- _sexYN_: is the post a sexual or lewd reference
- _offensiveYN_: could the post be offensive to anyone

Task 203:
could the post be offensive to anyone.

"""
import pandas as pd
import json

task = dict()

task['Contributors'] = ["Arlen Fan"]
task['Source'] = ["SBIC"]
task['Categories'] = ["Binary Classification"]
task['Definition'] = "You will be provided with a text input. Your task is to deduce if the post is " \
                     "is potentially offensive to anyone. Note that this can mean sexual, racial, religious biased " \
                     "or offensive language. You will answer 0 for No/This is not offensive to anyone, or 1 for " \
                     "Yes/This can be potentially offensive to a subset of people."

task['Positive Examples'] = [

    {
        "input": "#RPDR FUCKING FARRAH MOAN, HAVE YOU NEVER WATCHED THIS SHOW. WHEN YOU GET THE CALL, TAKE A LESSON.",
        "output": 1.0,
        "explanation": "(Correct Answer) This post is aggressive and berates a person for not having watched a show. Therefore the correct answer is 1/Potentially Offensive."
    },
    {
        "input": "I literally didn't even plan to live this long enough to experience aftershocks , I'm so scared of losing important things in my life \u2639\ufe0f",
        "output": 0.0,
        "explanation": "(Correct Answer) This post does not intend to offend and does not have any elements that make it offensive."
    },
    {
        "input": "to look at the bigger picture and see what this stupid and impulsive action done by our president means for us, what happens next?",
        "output": 1.0,
        "explanation": "(Correct Answer) This post is aggressive and is politically charged. Therefore the correct answer is 1/Potentially Offensive."
    }

]

task['Negative Examples'] = [
    {
        "input": "My sky sports news ain't working so I've gotta listen to that fucking clown Saunders &#128584;&#128584;&#128534;",
        "output": 0.0,
        "explanation": "(Incorrect Answer) This post is aggressive and is politically charged. Therefore the correct answer is 1/Potentially Offensive."
    },
    {
        "input": "We will always be going through it. But bitterness will assure that you will go through it humanly alone.",
        "output": 1.0,
        "explanation": "(Incorrect Answer) This post does not intend to offend and does not have any elements that make it offensive."
    },
    {
        "input": "Temp: 59.9\u00b0F Wind:4.5mph Pressure: 30.03mb Falling slowly Rain Today 0.00in. Forecast: Unsettled, precipitation later",
        "output": 1.0,
        "explanation": "(Incorrect Answer) This post does not intend to offend and does not have any elements that make it offensive."
    },
    {
        "input": "\"I hate all these \"\"safe spaces\"\" that people think they need. How about just live life? Oh, someone offended you! Do you know what you can -\"",
        "output": 1.0,
        "explanation": "(Incorrect Answer) This post is aggressive and ridicules the concept of safe spaces,"
        " a community where one can be free of judgment. Therefore the correct answer is 1/Potentially Offensive."
    }

]

task['Instances'] = []

# Read in data
df = pd.read_csv("SBIC.v2.trn.csv")

"""
100-6500 instances
"""

# need the offensiveYN, post columns only
col_list = ['offensiveYN', 'post']
df = df[col_list]

# filter out offensiveYN neq to 0 or 1
df = df[(df['offensiveYN'] == 0) | (df['offensiveYN'] == 1)]

# filter out duplicate posts
df = df.drop_duplicates()
# print(df)

# select 2000 of offensiveYN
df0 = df[df['offensiveYN'] == 0][0:2000]
df1 = df[df['offensiveYN'] == 1][0:2000]

print(df0)  # max index ----, can select pos and negative examples past this
print(df1)  # max index ----, can select pos and negative examples past this
# At this point, df0 contains 1000 label 0, df1 contains 1000 label 1

for post0, post1 in zip(df0.iterrows(), df1.iterrows()):
    text0 = post0[1][1]
    label0 = post0[1][0]
    text1 = post1[1][1]
    label1 = post1[1][0]
    task['Instances'].append({"input": text0, "output": label0})
    task['Instances'].append({"input": text1, "output": label1})

f = json.dumps(task, indent=4)
# Save filename
save_filename = 'task203_sbic_potentially_offense_binary_classification.json'
with open(save_filename, "w") as outfile:
    outfile.write(f)
