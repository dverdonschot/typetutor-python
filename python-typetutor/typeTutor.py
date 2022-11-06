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
    import functions

    unique_characters = set(characters)
    list_chars = list(unique_characters)

    training_chars = functions.charTrainingSet(numberOffLetters, list_chars)
    number_char = 0
    for i in training_chars:
        print(i)

        try:
            #while True:
                k = functions.getkey()
                if k == 'esc':
                    quit()
                if k == i:
                    number_char = number_char + 1
                    print (i + "= correct")
                    print(training_chars[:number_char])
                if k != i:
                    number_char = number_char + 1
                    print(k + " = wrong")
                    print(training_chars[:number_char])
                    
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

