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

    training_chars = functions.charTrainingSetLib(numberOffLetters, list_chars)
    number_char = 0
    for x, i in training_chars.items():
        print(terminal.magenta(i["character"]))

        try:
            #while True:
                k = functions.getkey()
                if k == 'esc':
                    print(terminal.yellow('quiting'))
                    quit()
                if k == i["character"]:
                    print (terminal.green(i["character"] + "= correct"))
                    print(training_chars[:(x + 1)])
                elif k != i["character"]:
                    print(terminal.red(k + " = wrong should be " + i["character"]))
                    k = functions.getkey()
                    if k != i["character"]:
                        print(terminal.red(k + " = still a fail should be " + i["character"]))
                    if k == i["character"]:
                        print (terminal.green(i["character"] + " = correct on second try"))
                        print(training_chars[:x + 1])
                    
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

