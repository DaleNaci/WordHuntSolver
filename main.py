import json
import time

from pprint import pprint

from trie import Trie


with open("words_dictionary.json", "r") as json_words:
    data = json.load(json_words)

trie = Trie()


def load_trie():
    for word in data.keys():
        trie.insert(word)


start = time.time()
load_trie()
end = time.time()
print(f"Seconds: {end - start}")
