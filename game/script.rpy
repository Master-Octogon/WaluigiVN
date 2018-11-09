# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Waluigi")


# The game starts here.

label start:

    "Waht, is my name?"
    $ input_test = renpy.input("Name: ")
    $ name = input_test.strip() or "Luigi"
    if name == "Waluigi":
        w"Correct!"
        w"It's Waluigi story time!"
    else:
        w"WRONG! My name is not [name]. My name is Waluigi."
        w"It's Waluigi story time."

    w"Time to test pathing"

    menu:
        "Which path?"
        "Path1":
            jump path1
        "Path2":
            jump path2
    return
