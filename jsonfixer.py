"""
This script is purely used to delete all of the words with 1 or 2 letters.
"""


import json


with open("words_dictionary.json", "r") as in_f:
    data = json.load(in_f)


for k in list(data.keys()).copy():
    if len(k) < 3:
        del data[k]


with open("words_dictionary.json", "w") as out_f:
    json.dump(data, out_f)
