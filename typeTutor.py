#!/usr/bin/python

from re import S
import typer
import sys,tty,os,termios
import typeTutorFunctions
import json

app = typer.Typer()

characterset = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^][)(}{~`|=.*+'\"-_"
letterset = "1234567890"
numpadset = "1234567890/+*-."
specialset = "!@#$%^][)(}{~`|=.*+'\"-_"

@app.callback()
def main():
    """
    Welcome to TypeTutor, Start Improving Your Typeskills Today!
    """
    print("Welcome to TypeTutor, Start Improving Your Typeskills Today!")

@app.command()
def random(characters: str = characterset, numberOffLetters: int = 100, secondtry: bool = True):
    """
    Train typing randomized characters from all over your keyboard, Letter, Numbers, special characters
    """
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomspecial(characters: str = specialset, numberOffLetters: int = 100, secondtry: bool = True):
    """
    Train typing Special Characters like ~[(){|@!$#^ in a randomized order
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomletters(characters: str = letterset, numberOffLetters: int = 50, secondtry: bool = True):
    """
    Train typing Letters 1234567890 in a randomized order
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomnumpad(characters: str = numpadset, numberOffLetters: int = 50, secondtry: bool = True):
    """
    Train typing the numpad keys including \+-*
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def words(name: str):
    """k
    Type random words sourced from the Linux words file.
    """
    print(f"Bye {name}!")

@app.command()
def quotes(secondtry: bool = False):
    """
    Type random quotes
    """
    quotesdict = json.load(open("quotes.json"))
    typeTutorFunctions.textTyper(quotesdict, secondtry=secondtry)


if __name__ == "__main__":
    app()

