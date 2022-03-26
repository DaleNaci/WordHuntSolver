import time
import turtle

import keyboard
from pprint import pprint

from trie import Trie
from word import Word
from letter import Letter


data = []
with open("data/2of12inf.txt", "r") as f:
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
    lttr = Letter(board[y][x], x, y)
    v.append(lttr)

    vc = vc.copy()
    vc.append([x, y])

    w = Word()
    for lttr in v:
        w.add_letter(lttr)

    if not trie.starts_with(w.get_word()):
        return
    elif len(w.get_word()) >= 3 and trie.search(w.get_word()):
        word_list.append(w)

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


word_list = sorted(word_list, key=lambda w: len(w.get_word()), reverse=True)

turtle.screensize(canvwidth=500, canvheight=500, bg="black")
turtle.speed(0)
turtle.hideturtle()
#turtle.done()
screen = turtle.getscreen()
screen.tracer(0)
t = turtle.Turtle()
t.color("white")


def draw_circle(r):
    t.up()
    start_pos = t.position()
    t.sety(t.position()[1] - r)
    t.down()
    t.circle(r)
    t.up()
    t.goto(start_pos)
    t.down()

finished_words = []

for word in word_list:
    if word.get_word() in finished_words:
        continue
    else:
        finished_words.append(word.get_word())

    first_lttr = True
    #input(word.get_word())
    t.up()
    for lttr in word.letters:
        x, y = lttr.get_coords()

        t.goto((x-1.5) * 100, (1.5-y) * 100)

        #print(f"{x}, {y}\t{(x-1.5) * 100}, {(1.5-y) * 100}")

        if first_lttr:
            first_lttr = False
            t.clear()

            start_pos = t.position()

            for x in range(-150, 250, 100):
                for y in range(-150, 250, 100):
                    t.color("red")
                    t.up()
                    t.goto(x, y)
                    t.down()
                    draw_circle(5)
                    t.color("white")

            t.up()
            t.goto(start_pos)
            t.down()

            t.color("green")
            draw_circle(15)
            t.color("white")

    screen.update()

    input(word.get_word())
