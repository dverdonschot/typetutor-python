#!/usr/bin/python

from re import S
import typer
import random
import sys,tty,os,termios
import typeTutorFunctions

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
def randomcharacters(characters: str = characterset, numberOffLetters: int = 100, secondtry: bool = True):
    """
    Train typing randomized characters, Letter, Numbers, special characters
    """
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomspecial(characters: str = specialset, numberOffLetters: int = 100, secondtry: bool = True):
    """
    Train typing Special Characters in a randomized order
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomletters(characters: str = letterset, numberOffLetters: int = 50, secondtry: bool = True):
    """
    Train typing Letters in a randomized order
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

@app.command()
def randomnumpad(characters: str = numpadset, numberOffLetters: int = 50, secondtry: bool = True):
    """
    Train typing the numpad keys
    """
    import typeTutorFunctions
    typeTutorFunctions.randomTyper(characters, numberOffLetters=numberOffLetters, secondtry=secondtry)

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

