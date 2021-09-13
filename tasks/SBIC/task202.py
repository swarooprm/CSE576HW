"""

Notes:
- _intentYN_: was the intent behind the statement to offend
- _sexYN_: is the post a sexual or lewd reference
- _offensiveYN_: could the post be offensive to anyone

Task 202:
Is this phrase a refernce to sexual explicit content or lewd reference? Binary classification.

"""
import pandas as pd
import json

task = dict()

task['Contributors'] = ["Arlen Fan"]
task['Source'] = ["SBIC"]
task['Categories'] = ["Binary Classification"]
task['Definition'] = "You will be provided with a text input. Your task is to deduce if the post is " \
                     "is sexually offensive. Emphasis on sexually offensive or any lewd reference. " \
                     "Please consider offensive posts that do not reference sexually explicit content. For " \
                     "example, religious or racially offensive posts need not be lewd in nature. You must answer 0" \
                     " for No/This is NOT a sexually explicit post and 1 for " \
                     "Yes/This is a sexually explicit post."

task['Positive Examples'] = [
    {
        "input": "\"Ghost in the Shell makes $19M, a lot less than expected. Now write some hot takes for \"\"why Marvel never made a standalone Black Widow movie\"\"\"",
        "output": 0.0,
        "explanation": "(Correct Answer) This post does not reference sexually explicity or lewd content."
    },
    {
        "input": "ok yea i listen to weird music but this guy is playing some metal mexican rap shit and I really need to leave this class",
        "output": 0.0,
        "explanation": "(Correct Answer) This post does not reference sexually explicity or lewd content. Even though it uses offensive language, it is not lewd."
    },
    {
        "input": "george michaels q. what 's white and sticky and found on the bathroom wall ? a. george michael 's latest release .",
        "output": 1.0,
        "explanation": "(Correct Answer) This post references semen, and is therefore considered sexually explicit."
    }

]

task['Negative Examples'] = [

    {
        "input": "Don't tell me what I am or what I've been through ,, ya fucking fat ugly cunT",
        "output": 1.0,
        "explanation": "(Incorrect Answer) This post references the word 'cunt,' a vulgar slang for female genitalia, but this word also means something else in this context."
    },
    {
        "input": "the chances of you getting laid . <repeat> . <repeat> re about equal to the chances of oscar pistorius catching athlete 's foot from sharing a bathroom with his girlfriend",
        "output": 0.0,
        "explanation": "(Incorrect Answer) This post features a reference to catching sexually transmitted disease and is therefore considered sexually explicit or lewd."
    },
    {
        "input": "niggas wanted women rights trans rights gay rights asian rights muslim rights mexican rights\u2026 y\u2019all want inclusion there you have it",
        "output": 1.0,
        "explanation": "(Incorrect Answer) This post is racially charged and offensive, but does not contain any reference to sexually explicit content."
    }

]

task['Instances'] = []

# Read in data
df = pd.read_csv("SBIC.v2.trn.csv")

"""
100-6500 instances
"""

# need the sexYN, post columns only
col_list = ['sexYN', 'post']
df = df[col_list]

# filter out sexYN neq to 0 or 1
df = df[(df['sexYN'] == 0) | (df['sexYN'] == 1)]

# filter out duplicate posts
df = df.drop_duplicates()
# print(df)

# select 2000 of intentYN == 0 and intentYN == 1
df0 = df[df['sexYN'] == 0][0:2000]
df1 = df[df['sexYN'] == 1][0:2000]

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
save_filename = 'task202_sbic_sexual_offense_binary_classification.json'
with open(save_filename, "w") as outfile:
    outfile.write(f)
