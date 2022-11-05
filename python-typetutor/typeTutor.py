#!/usr/bin/python

import typer
import random
import sys,tty,os,termios

app = typer.Typer()

characterset = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^][)(}{~`|=.*+'"

@app.command()
def traincharacters(characters: str = characterset, numberOffLetters: int = 100):
    """
    Type the characters you want to train.
    You will get the characters randomized.
    """
    unique_characters = set(characters)
    list_chars = list(unique_characters)
    print(list_chars[1])

    def getkey():
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        try:
            while True:
                b = os.read(sys.stdin.fileno(), 3).decode()
                if len(b) == 3:
                    k = ord(b[2])
                else:
                    k = ord(b)
                key_mapping = {
                    127: 'backspace',
                    10: 'return',
                    32: 'space',
                    9: 'tab',
                    27: 'esc',
                    65: 'up',
                    66: 'down',
                    67: 'right',
                    68: 'left'
                }
                return key_mapping.get(k, chr(k))
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
    def charTrainingSet(number, characters):

        generated_charTrainingSet = []
        for i in range(number):
            generated_charTrainingSet.append(random.choice(characters))
        return generated_charTrainingSet

    training_chars = charTrainingSet(numberOffLetters, list_chars)
    number_char = 0
    for i in training_chars:
        
        print(i)

        try:
            #while True:
                k = getkey()
                if k == 'esc':
                    quit()
                if k == i:
                    number_char + 1
                    print (i + "= correct")
                    print(training_chars[:number_char])
                else:
                    print(k + " = wrong")

        except (KeyboardInterrupt, SystemExit):
            os.system('stty sane')
            print('stopping.')



@app.command()
def words(name: str):
    """
    Type random words sourced from the Linux words file.
    """
    print(f"Bye {name}!")

@app.command()
def quotes(name: str):
    """
    Type random quotes
    """
    print(f"Bye {name}!")

if __name__ == "__main__":
    app()

