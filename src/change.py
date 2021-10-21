#!/usr/bin/env python3
import json
import random
from os import listdir
from os.path import isfile, join

# read all the tasks and make sure that they're following the right pattern
tasks_path = '../tasks/'

expected_keys = [
    "Definition",
    "Positive Examples",
    "Negative Examples",
    "Instances",
    'Contributors',
    'Categories',
    'Source'
]

files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort()

for file in files:
  if ".md" not in file:
    print(f" --> testing file: {file}")
    assert '.json' in file, 'the file does not seem to have a .json in it: ' + file
    file_path = tasks_path + file
    data = None
    with open(file_path, 'r', encoding="utf-8") as f:
      data = json.load(f)
      for key in expected_keys:
        assert key in data, f'did not find the key: {key}'
      
      # for x in range(len(data["Positive Examples"])):
      #   if type(data['Positive Examples'][x]["input"]) != str:
      #     data['Positive Examples'][x]["input"] = json.dumps(data['Positive Examples'][x]["input"])
      #   pass
      # for x in range(len(data["Negative Examples"])):
      #   if type(data['Negative Examples'][x]["input"]) != str:
      #     data['Negative Examples'][x]["input"] = json.dumps(data['Negative Examples'][x]["input"])
      #   pass
      # for x in range(len(data["Instances"])):
      #   if type(data['Instances'][x]["input"]) != str:
      #     data['Instances'][x]["input"] = json.dumps(data['Instances'][x]["input"])
      #   pass
      
      # for x in range(len(data['Instances'])):
      #   if type(data['Instances'][x]["output"]) != list:
      #     data['Instances'][x]["output"] = [data['Instances'][x]["output"]]
      # for x in range(len(data['Instances'])):
      #   data['Instances'][x]["output"] = list(set(data['Instances'][x]["output"]))
      ds = {}
      for i in data["Instances"]:
        k = json.dumps(i["input"])
        if k in ds:
          if i["output"]:
            ds[k]["output"].append(i["output"][0])
            ds[k]["output"] = list(set(ds[k]["output"]))
        else:
          ds[k] = i
      data["Instances"] = list(ds.values())
    x = list(data["Instances"])
    random.shuffle(x)
    data["Instances"] = x
    with open(file_path, 'w', encoding="utf-8") as f:
      json.dump(data, f, indent=4, ensure_ascii=False)
print("Done")

              