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

task = dict()

task['Contributors'] = ["Arlen Fan"]
task['Source'] = ["SBIC"]
task['Categories'] = ["Binary Classification"]
task['Definition'] = "You will be provided with a text input. Your task is to deduce if the post is " \
                     "intentionally offensive. Please closely consider offensive statements that appear to " \
                     "be unintentional, or non-offensive statements that are underhandedly offensive. " \
                     "Your answer is a simple yes/no or True/False response, indicating if you believe a " \
                     "sentence/paragraph is intentionally offensive. Please answer 0 for No (not intentionally offensive) and answer 1 " \
                     "for Yes (intentionally offensive)."

task['Positive Examples'] = [
    {
        "input": "Living alone rocks. Being sick and living alone sucks. Will bake someone many a baked good for some "
                 "NyQuil / DayQuil rn.",
        "output": 0.0,
        "explanation": "This is a good example of a post that is not intended to offend. There is no sign of intention "
                       "to offend and no offensive language is used. This is simply a post about the pitiful state of the poster."
    },
    {
        "input": "@hi_imkadie I wouldn't know cause i don't fuck with these hoes",
        "output": 1.0,
        "explanation": "This is a good example of an offensive post, because it uses both offensive language and "
                       "has an aggressive undertone."
    },
]

task['Negative Examples'] = [
    {
        "input": "@Midnight_Snacka bitches like u be proving my point, u speak on shit u know nothing about I got a fucking at studio movie grill just stfu",
        "output": 0.0,
        "explanation": "(Answer is incorrect) This is clearly an example of an offensive post, because it uses both offensive language and "
                       "has an aggressive undertone."
    },
    {
        "input": "i just got a flashback to after the wwa tour when my dad was parked by the shedd waiting to pick us up wtf",
        "output": 1.0,
        "explanation": "(Answer is incorrect) Although this uses some expletive language like 'wtf', this is not considered offensive because "
                       "the post does not seem to be aggressive or intend to attack anything."
    },
]

task['Instances'] = []

# Read in data
df = pd.read_csv("SBIC.v2.trn.csv")

"""
100-6500 instances
"""

# need the intentYN, post columns only
col_list = ['intentYN', 'post']
df = df[col_list]

# filter out intent YN neq to 0 or 1
df = df[(df['intentYN'] == 0) | (df['intentYN'] == 1)]

# filter out duplicate posts
df = df.drop_duplicates()
# print(df)

# select 500-1000 of intentYN == 0 and intentYN == 1
df0 = df[df['intentYN'] == 0][0:1000]
df1 = df[df['intentYN'] == 1][0:1000]

# print(df0) #max index 8767, can select pos and negative examples past this
# print(df1) #max index 4578, can select pos and negative examples past this
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
save_filename = 'task201_sbic_intentional_offense_binary_classification.json'
with open(save_filename, "w") as outfile:
    outfile.write(f)
