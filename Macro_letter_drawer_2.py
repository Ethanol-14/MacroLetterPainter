from pynput.keyboard import Key, Controller as KeyCon
from pynput.mouse import Button, Controller as ButCon
import keyboard
import time

keys = KeyCon()
mouse = ButCon()

print("Type font size (not accurate to word)")
fontsize = input()
fontsize = int(fontsize)
print("Put your mouse where you want the typing to start and press enter")
input()

startingxpos = mouse.position[0]

delay = 0.01

def lift(_x, _y, _size):
    mouse.move(_x*_size, -_y*_size)

def ink(_x, _y, _size):
    delay = 0.01
    mouse.press(Button.left)
    time.sleep(delay)
    mouse.move(_x*_size, -_y*_size)
    time.sleep(delay)
    mouse.release(Button.left)

def draw(_character):
    delay = 0.01

    letters = " 1234567890qwertyuiopasdfghjklzxcvbnm,.-'"
    count = 0

    #space
    count = count+1

    #1
    if _character == letters[count]:
        ink(2, 0, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        lift(0, -3, fontsize)
    count = count+1

    #2
    if _character == letters[count]:
        lift(0, 3, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-2, -3, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #3
    if _character == letters[count]:
        lift(0, 3, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #4
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #5
    if _character == letters[count]:
        ink(1, 0, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

    #6
    if _character == letters[count]:
        lift(2, 3, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #7
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        ink(-2, -4, fontsize)
    count = count+1

    #8
    if _character == letters[count]:
        lift(1, 0, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        lift(0, 2, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        lift(-1, -2, fontsize)
    count = count+1

    #9
    if _character == letters[count]:
        lift(2, 0, fontsize)
        time.sleep(delay)
        ink(0, 3, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        lift(-2, -3, fontsize)
    count = count+1

    #0
    if _character == letters[count]:
        lift(0, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #q
    if _character == letters[count]:
        lift(0, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        lift(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #w
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        ink(1, 2, fontsize)
        time.sleep(delay)
        ink(1, -2, fontsize)
        time.sleep(delay)
        ink(0, 4, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

    #e
    if _character == letters[count]:
        lift(2, 4, fontsize)
        time.sleep(delay)
        ink(-2, 0, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, 2, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, -2, fontsize)
    count = count+1

    #r
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        lift(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -2, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #t
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-1, 0, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        lift(-1, 0, fontsize)
    count = count+1

    #y
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(1, -2, fontsize)
        time.sleep(delay)
        ink(1, 2, fontsize)
        time.sleep(delay)
        lift(-1, -2, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        lift(-1, 0, fontsize)
    count = count+1

    #u
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(0, -3, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 3, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

    #i
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-1, 0, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        lift(1, 0, fontsize)
        time.sleep(delay)
        ink(-2, 0, fontsize)
    count = count+1

    #o
    if _character == letters[count]:
        lift(0, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #p
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        lift(0, -2, fontsize)
    count = count+1

    #a
    if _character == letters[count]:
        ink(0, 3, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(0, -3, fontsize)
        time.sleep(delay)
        lift(0, 2, fontsize)
        time.sleep(delay)
        ink(-2, 0, fontsize)
        time.sleep(delay)
        lift(0, -2, fontsize)
    count = count+1

    #s
    if _character == letters[count]:
        lift(2, 3, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(2, -2, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #d
    if _character == letters[count]:
        ink(1, 0, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 2, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
    count = count+1

    #f
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(0, -2, fontsize)
        time.sleep(delay)
        ink(-2, 0, fontsize)
        time.sleep(delay)
        lift(0, -2, fontsize)
    count = count+1

    #g
    if _character == letters[count]:
        lift(2, 3, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 1, fontsize)
        time.sleep(delay)
        ink(0, 1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        lift(-1, -2, fontsize)
    count = count+1

    #h
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        lift(0, -2, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(0, 2, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #j
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        ink(0, -3, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 1, fontsize)
        time.sleep(delay)
        lift(0, -1, fontsize)
    count = count+1

    #k
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        lift(2, 0, fontsize)
        time.sleep(delay)
        ink(-2, -2, fontsize)
        time.sleep(delay)
        ink(2, -2, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #l
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #z
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        ink(-2, -4, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #x
    if _character == letters[count]:
        ink(2, 4, fontsize)
        time.sleep(delay)
        lift(0, -4, fontsize)
        time.sleep(delay)
        ink(-2, 4, fontsize)
        time.sleep(delay)
        lift(0, -4, fontsize)
    count = count+1

    #c
    if _character == letters[count]:
        lift(2, 4, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(0, -2, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(1, 0, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #v
    if _character == letters[count]:
        lift(0, 4, fontsize)
        time.sleep(delay)
        ink(1, -4, fontsize)
        time.sleep(delay)
        ink(1, 4, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

    #b
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
        time.sleep(delay)
        lift(1, 0, fontsize)
        time.sleep(delay)
        ink(1, -1, fontsize)
        time.sleep(delay)
        ink(-1, -1, fontsize)
        time.sleep(delay)
        ink(-1, 0, fontsize)
    count = count+1

    #n
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(2, -4, fontsize)
        time.sleep(delay)
        ink(0, 4, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

    #m
    if _character == letters[count]:
        ink(0, 4, fontsize)
        time.sleep(delay)
        ink(1, -2, fontsize)
        time.sleep(delay)
        ink(1, 2, fontsize)
        time.sleep(delay)
        ink(0, -4, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #,
    if _character == letters[count]:
        ink(0, -1, fontsize)
        time.sleep(delay)
        lift(-2, 1, fontsize)
    count = count+1

    #.
    if _character == letters[count]:
        ink(0, 0, fontsize)
        time.sleep(delay)
        lift(-2, 0, fontsize)
    count = count+1

    #-
    if _character == letters[count]:
        lift(0, 2, fontsize)
        time.sleep(delay)
        ink(2, 0, fontsize)
        time.sleep(delay)
        lift(-2, -2, fontsize)
    count = count+1

    #'
    if _character == letters[count]:
        lift(0, 3, fontsize)
        time.sleep(delay)
        ink(0, 1, fontsize)
        time.sleep(delay)
        lift(-2, -4, fontsize)
    count = count+1

while True:
    print("Type what you wanna write with your mouse")
    print("Use / for enter")
    sentence = input()

    for i in sentence:
        if i == "/":
            mouse.position = (startingxpos, mouse.position[1]+(5*fontsize))

        if i == " ":
            mouse.release(Button.left)
            time.sleep(delay)
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "1":
            draw("1")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "2":
            draw("2")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "3":
            draw("3")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "4":
            draw("4")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "5":
            draw("5")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "6":
            draw("6")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "7":
            draw("7")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "8":
            draw("8")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "9":
            draw("9")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "0":
            draw("0")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "q":
            draw("q")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "w":
            draw("w")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "e":
            draw("e")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "r":
            draw("r")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "t":
            draw("t")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "y":
            draw("y")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "u":
            draw("u")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "i":
            draw("i")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "o":
            draw("o")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "p":
            draw("p")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "a":
            draw("a")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "s":
            draw("s")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "d":
            draw("d")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "f":
            draw("f")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "g":
            draw("g")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "h":
            draw("h")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "j":
            draw("j")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "k":
            draw("k")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "l":
            draw("l")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "z":
            draw("z")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "x":
            draw("x")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "c":
            draw("c")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "v":
            draw("v")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "b":
            draw("b")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "n":
            draw("n")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "m":
            draw("m")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == ",":
            draw(",")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == ".":
            draw(".")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "-":
            draw("-")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])

        if i == "'":
            draw("'")
            mouse.position = (mouse.position[0]+(3*fontsize), mouse.position[1])
