"""

Notes:

Task 204:
Label proper nouns and noun phrases

"""
import pandas as pd
import json

task = dict()

task['Contributors'] = ["Arlen Fan"]
task['Source'] = ["SBIC"]
task['Categories'] = ["Binary Classification"]
task[
    'Definition'] = "You will be provided with a text input. Your task is to find all of the proper nouns and label them. The possible " \
                    "labels are persons <B-PER>, <I-PER>, organizations <B-ORG>, <I-ORG>, " \
                    "locations <B-LOC>, <I-LOC>, and other <B-MISC>, <I-MISC>. The capital B denotes " \
                    "the first word of a proper noun phrase. The " \
                    "capital I denotes all following words of the SAME noun phrase." \
                    " For example West Virginia would be labeled as " \
                    "West <B-LOC> Virginia <I-LOC>. Manchester United would be labeled as Manchester <B-ORG> United <I-LOC>." \
                    "The person whose first name is John and last name is Doe and called John Doe would be labeled as " \
                    "John <B-PER> Doe <I-PER>. If a word is not a part of a proper noun phrase, do not label it."

task['Positive Examples'] = [
    {
        "input": "It has manufacturing plants in San Diego ; Creedmoor , N.C. ; Hampshire , England ; and Tijuana , Mexico , and distributes its prodcuts in more than 120 countries . ",
        "output":
            "It has manufacturing plants in San <B-LOC> Diego <I-LOC> ; Creedmoor <B-LOC> , N.C. <B-LOC> ; Hampshire <B-LOC> , England <B-LOC> ; and Tijuana <B-LOC> , Mexico <B-LOC> , and distributes its prodcuts in more than 120 countries . "
        ,
        "explanation": "This is how the labeling should be. San Diego is the name of a location. In addition, "
                       "it cannot be separated and is represented by two words. Therefore the labeling is San <B-LOC> Diego <I-LOC>. "
                       "For the other locations mentioned in this sentence, they are single word locations and are represented with the label "
                       "<B-LOC>."
    },
    {
        "input": "Eli Lilly sold IVAC on Dec. 31 , 1994 to DLJ Merchant Banking Partners LP , River Medical Inc. and other investors . ",
        "output":
            "Eli <B-ORG> Lilly <I-ORG> sold IVAC <B-ORG> on Dec. 31 , 1994 to DLJ <B-ORG> Merchant <I-ORG> Banking <I-ORG> Partners <I-ORG> LP <I-ORG> , River <B-ORG> Medical <I-ORG> Inc. <I-ORG> and other investors . "
        ,
        "explanation":"Eli Lilly a two-word representation of a company. Therefore, it gets the label Eli <B-ORG> Lilly <I-ORG>. IVAC "
                      "is the name of a company. It gets IVAC <B-ORG>. DLJ Merchant Banking Partners LP is a five-word proper "
                      "noun phrase and therefore gets the label "
                      "DLJ <B-ORG> Merchant <I-ORG> Banking <I-ORG> Partners <I-ORG> LP <I-ORG>. River Medical Inc. is the "
                      "name of a three word noun phrase and gets the label River <B-ORG> Medical <I-ORG> Inc. <I-ORG>."
    },
    {
        "input": "That is why I will no longer be deputy by the time the film opens . \" ",
        "output":
            "That is why I will no longer be deputy by the time the film opens . \" "
        ,
        "explanation":"This is the correct labeling (no labels), because the sentence does not contain any proper noun or noun phrases."
    }
]

task['Negative Examples'] = [
    {
        "input": "The merger will add to both companies ' historical leadership in infusion therapy and technology-based drug delivery devices , they said . ",
        "output":
            "The merger <B-MISC> will add to both companies ' historical leadership in infusion therapy and technology-based drug delivery devices , they said . "
        ,
        "explanation": "This is incorrect. The 'merger' is not a proper noun and should not receive any tag. The correct labeling of the sentence "
                       "is that NO tags are added."
    },
    {
        "input": "It did not say when the charge would be taken . ",
        "output":
            "It did not say when the charge <B-MISC> would be taken . "
        ,
        "explanation": "This is incorrect. The 'charge' is not a proper noun and should not receive any tag. The correct labeling of the sentence "
                       "is that NO tags are added."
    }

]

task['Instances'] = []

# newfile is the file object , devops.txt is the file to be opened and default Access mode is read
newfile = open('conllpp_train.txt', 'r')
read_content = newfile.read()
read_content = read_content.split('-DOCSTART- -X- -X- O')

duplicate_finder = set()
for i in read_content:
    sentence = (i.split('\n\n'))
    for num, j in enumerate(sentence):
        lines = j.split('\n')
        if len(lines) == 1:
            continue

        original_sentence = ''
        sentence = ''
        for k in lines:
            word = k.split(' ')[0]
            label = k.split(' ')[3]
            # print(word,label)
            sentence += word + ' '
            original_sentence += word + ' '
            if label == 'O':
                continue
            # else
            sentence += '<' + label + '> '

        if original_sentence in duplicate_finder:
            continue
        duplicate_finder.add(original_sentence)
        task['Instances'].append(
            {
                "input": original_sentence,
                "output": [sentence]
            }
        )

        if (len(task['Instances'])) > 3000:
            break

"""
100-6500 instances
"""

print(len(task['Instances']))

f = json.dumps(task, indent=4)
# Save filename
save_filename = 'task204_conllpp_ner.json'
with open(save_filename, "w") as outfile:
    outfile.write(f)
