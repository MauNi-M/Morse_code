from play_beep import *

# Code from https://math.hws.edu/eck/cs225/s03/code.txt
code = []
with open("code.txt", "r") as code_file:
    for line in code_file:
        code.append(line)
code_dict = {item.split()[0]:item.split()[1] for item in code}
sounds_dict ={"-": play_dah, ".": play_dit}
sentence = input("What do you want to say in Morse?>").upper()
for letter in sentence:
    if letter == " ":
        word_gap()
        continue
    print(f"{letter}: {code_dict[letter]}")
    for symb in code_dict[letter]:
        sounds_dict[symb]()
    letter_gap()


