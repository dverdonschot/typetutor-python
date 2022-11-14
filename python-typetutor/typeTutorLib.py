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
    import datetime

    unique_characters = set(characters)
    list_chars = list(unique_characters)

    training_chars = functions.charTrainingSetLib(numberOffLetters, list_chars)

    for x, i in training_chars.items():
        print(terminal.magenta(i["character"]))
        start_char = datetime.datetime.now()

        try:
            k = functions.getkey()
            if k == 'esc':
                print(terminal.yellow('quiting'))
                quit()
            if k == i["character"]:
                duration_char = datetime.datetime.now() - start_char
                i.update({"userinput": "correct","duration": str(duration_char)})
                print (terminal.green(i["character"] + " = correct in " + i["duration"]))
                functions.colorizedTypedString(training_chars, (x + 1))
            elif k != i["character"]:
                print(terminal.red(k + " = wrong should be " + i["character"]))
                k = functions.getkey()
                if k != i["character"]:
                    i.update({"userinput": "incorrect","duration": "na"})
                    print(terminal.red(k + " = still a fail should be " + i["character"]))
                    functions.colorizedTypedString(training_chars, (x + 1))
                if k == i["character"]:
                    duration_char = datetime.datetime.now() - start_char
                    i.update({"userinput": "second_try","duration": str(duration_char)})
                    print (terminal.green(i["character"] + " = correct on second try in " + i["duration"]))
                    functions.colorizedTypedString(training_chars, (x + 1))
                
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

