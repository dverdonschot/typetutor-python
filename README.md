# TypeTutor

Typetutor is a python commandline (cli) program to help you improve your touch typing skills.
It allows you to train keys by typing random character selections, like letters, special or all characters.

## Options currently available

```
python3 typeTutor.py --help
python3 typeTutor.py random
python3 typeTutor.py randomletters
python3 typeTutor.py randomnumpad
python3 typeTutor.py randomspecial --characters "[({~" --numberoffletters 10 --secondtry
```

## customize the typing challenges
Using the CLI options you can tune your settings and select characters or the amount of characters you have to type.

```
python3 typeTutor.py randomletters --characters 12345678 --numberoffletters 100
```

## Roadmap
Next feature to implement is typing quotes, followed by typing code.

