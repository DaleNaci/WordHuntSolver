import time

import keyboard
from pprint import pprint

from trie import Trie


data = []
with open("corncob_lowercase.txt", "r") as f:
    for line in f.readlines():
        data.append(line.strip())

trie = Trie()
board = []
word_list = []


def load_trie():
    for word in data:
        trie.insert(word)


def fill_board():
    for i in range(4):
        row = input()
        board.append([c for c in row])
    pprint(board)


# x = x-coordinate
# y = y-coordinate
# v = visited
# vc = visited coords
def f(x, y, v, vc):
    v = v.copy()
    v.append(board[y][x])

    vc = vc.copy()
    vc.append([x, y])

    word = "".join(v)
    
    if not trie.starts_with(word):
        return
    elif len(word) >= 3 and trie.search(word):
        word_list.append(word)

    if x != 3 and [x+1, y] not in vc:
        f(x+1, y, v, vc)
    if x != 0 and [x-1, y] not in vc:
        f(x-1, y, v, vc)

    if y != 3 and [x, y+1] not in vc:
        f(x, y+1, v, vc)
    if y != 0 and [x, y-1] not in vc:
        f(x, y-1, v, vc)

    if x != 3 and y != 3 and [x+1, y+1] not in vc:
        f(x+1, y+1, v, vc)
    if x != 3 and y != 0 and [x+1, y-1] not in vc:
        f(x+1, y-1, v, vc)
    if x != 0 and y != 3 and [x-1, y+1] not in vc:
        f(x-1, y+1, v, vc)
    if x != 0 and y != 0 and [x-1, y-1] not in vc:
        f(x-1, y-1, v, vc)
    



def find_words():
    for i in range(4):
        for j in range(4):
            f(i, j, [], [])


print("Give all 4 rows below:")
fill_board()
load_trie()
find_words()

word_list = list(set(word_list))

word_list.sort(key=lambda s: len(s), reverse=True)

for word in word_list:
   input(word)
