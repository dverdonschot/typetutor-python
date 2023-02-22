#!/usr/bin/python

import typer
import random
import sys,tty,os,termios


app = typer.Typer()

characterset = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^][)(}{~`|=.*+'\"-_"
letterset = "1234567890"
numpadset = "1234567890/+*-."
specialset = "!@#$%^][)(}{~`|=.*+'\"-_"

@app.command()
def randomcharacters(characters: str = characterset, numberOffLetters: int = 100):
    """
    Train typing randomized characters, Letter, Numbers, special characters
    """
    import randomFunctions
    randomFunctions.randomcharacters(characters, numberOffLetters=numberOffLetters)

def randomspecial(characters: str = specialset, numberOffLetters: int = 100):
    """
    Train typing Special Characters in a randomized order
    """
    import randomFunctions
    randomFunctions.randomcharacters(characters, numberOffLetters=numberOffLetters)

@app.command()
def randomletters(characters: str = letterset, numberOffLetters: int = 50):
    """
    Train typing Letters in a randomized order
    """
    import randomFunctions
    randomFunctions.randomcharacters(characters, numberOffLetters=numberOffLetters)

@app.command()
def randomnumpad(characters: str = numpadset, numberOffLetters: int = 50):
    """
    Train typing the numpad keys
    """
    import randomFunctions
    randomFunctions.randomcharacters(characters, numberOffLetters=numberOffLetters)


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

