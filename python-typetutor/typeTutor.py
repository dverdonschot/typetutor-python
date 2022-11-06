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
    import terminal

    unique_characters = set(characters)
    list_chars = list(unique_characters)

    training_chars = functions.charTrainingSet(numberOffLetters, list_chars)
    number_char = 0
    for i in training_chars:
        print(terminal.magenta(i))

        try:
            #while True:
                k = functions.getkey()
                if k == 'esc':
                    print(terminal.yellow('quiting'))
                    quit()
                if k == i:
                    number_char = number_char + 1
                    print (terminal.green(i + "= correct"))
                    print(training_chars[:number_char])
                elif k != i:
                    number_char = number_char + 1
                    print(terminal.red(k + " = wrong should be " + i))
                    k = functions.getkey()
                    if k != i:
                        print(terminal.red(k + " = still a fail should be " + i))
                    if k == i:
                        print (terminal.green(i + " = correct on second try"))
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

