import random
import sys,tty,os,termios
import terminal

def getkey():
    """get the user input from keyboard press"""
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
            #    65: 'up',
            #    66: 'down',
            #    67: 'right',
            #    68: 'left'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def charTrainingSetLib(number, characters):
    """Create a list of random characters that the user has to type as training"""
    generated_charTrainingSetLib = {}
    for i in range(number):
        generated_charTrainingSetLib.update({i: {"character": random.choice(characters), "userinput": "", "duration": ""}})
    return generated_charTrainingSetLib

def textTrainingSetLib(text):
    """Create a list of characters from a text like a quote, that the user can then type as training"""
    generated_charTrainingSetLib = {}
    item_number = 0
    for i in text:
        item_number += 1
        print(i)
        generated_charTrainingSetLib.update({item_number: {"character": i, "userinput": "", "duration": ""}})
    return generated_charTrainingSetLib

def colorizedTypedString(dictTrainingSet: dict, iteration: int, showAll: bool = False ):
    """Created a colorized string with all typed charaters"""
    import terminal

    for x, i in dictTrainingSet.items():
        if x >= (iteration):
            if showAll == False:
                break
            if showAll == True:
                print(terminal.white(i["character"]), end='')
        if i["userinput"] == "correct":
            print(terminal.green(i["character"]), end='')
        if i["userinput"] == "incorrect":
            print(terminal.red(i["character"]), end='')
        if i["userinput"] == "second_try":
            print(terminal.blue(i["character"]), end='')
        else:
            print('', end='')
    print("", end="\n")

def summaryResults(dictTrainingSet, secondtry: bool = False):
  import datetime
  import re
  import statistics
  pattern_timestamp = '([0-9]{1}:[0-9]{2}:[0-9]{2}.[0-9]{6})'
  correct = 0
  second_try = 0
  incorrect = 0
  average_deciseconds_list = []
  for x, i in dictTrainingSet.items():
    if i["userinput"] == 'correct':
      correct += 1
    if i["userinput"] == 'incorrect':
      incorrect += 1
    if secondtry == True and i["userinput"] == 'second_try':
      second_try += 1

    if re.match(pattern_timestamp, i["duration"]):
        timestamp_obj = datetime.datetime.strptime(i["duration"], '%H:%M:%S.%f')
        duration_decisecond = int((timestamp_obj.second * 1000000 + timestamp_obj.microsecond) / 10000)
        average_deciseconds_list.append(duration_decisecond)

  average_duration = int(statistics.mean(average_deciseconds_list)) / 100

  return_var = """##################################################
  Typed First Time Right: {correct}
  Failed to type correct: {incorrect}
  Average Duration per Typed Character: {average_duration}
  """.format(correct=correct, incorrect=incorrect, average_duration=average_duration)

  return_var_secondtry = """##################################################
  Typed First Time Right: {correct}
  Needed a Second Try: {second_try}
  Failed to type correct: {incorrect}
  Average Duration per Typed Character: {average_duration}
  """.format(correct=correct, second_try=second_try, incorrect=incorrect, average_duration=average_duration)

  return_result = return_var if secondtry == False else return_var_secondtry

  return return_result

def randomTyper(characters: str, numberOffLetters: int, secondtry: bool = False):
    """
    Type the characters you want to train.
    You will get the characters randomized.
    """
    import typeTutorFunctions
    import terminal
    import datetime

    unique_characters = set(characters)
    list_chars = list(unique_characters)

    training_chars = typeTutorFunctions.charTrainingSetLib(numberOffLetters, list_chars)

    for x, i in training_chars.items():
        print(terminal.magenta(i["character"]))
        start_char = datetime.datetime.now()

        try:
            k = typeTutorFunctions.getkey()
            if k == 'esc':
                print(terminal.yellow('quiting'))
                quit()
            if k == i["character"]:
                duration_char = datetime.datetime.now() - start_char
                i.update({"userinput": "correct","duration": str(duration_char)})
                print (terminal.green(i["character"] + " = correct in " + i["duration"]))
                typeTutorFunctions.colorizedTypedString(training_chars, (x + 1))
            elif k != i["character"]:
                print(terminal.red(k + " = wrong should be " + i["character"]))
                if secondtry == False:
                    i.update({"userinput": "incorrect", "duration": "na"})
                    typeTutorFunctions.colorizedTypedString(training_chars, (x + 1))
                elif secondtry == True:
                    k = typeTutorFunctions.getkey()
                    if k != i["character"]:
                        i.update({"userinput": "incorrect","duration": "na"})
                        print(terminal.red(k + " = still a fail should be " + i["character"]))
                        typeTutorFunctions.colorizedTypedString(training_chars, (x + 1))
                    if k == i["character"]:
                        duration_char = datetime.datetime.now() - start_char
                        i.update({"userinput": "second_try","duration": str(duration_char)})
                        print (terminal.green(i["character"] + " = correct on second try in " + i["duration"]))
                        typeTutorFunctions.colorizedTypedString(training_chars, (x + 1))
        except (KeyboardInterrupt, SystemExit):
            os.system('stty sane')
            print('stopping.')

    print(typeTutorFunctions.summaryResults(training_chars, secondtry))

def textTyper(text: dict, secondtry: bool = False):
    """
    Type text from like quotes from a quotes file
    """
    import typeTutorFunctions
    import terminal
    import datetime

    length_text = len(text)
    randomquote = random.randint(0, (length_text - 1))
    print(text[randomquote]['quote'])
    print(text[randomquote]['author'])


    characterlib = textTrainingSetLib(text[randomquote]['quote'])
    print(characterlib)

    typeTutorFunctions.colorizedTypedString(characterlib, (0), showAll=True)

    for x, i in characterlib.items():
        print(terminal.magenta(i["character"]))
        start_char = datetime.datetime.now()


        try:
            k = typeTutorFunctions.getkey()
            if k == 'esc':
                print(terminal.yellow('quiting'))
                quit()
            if k == i["character"]:
                duration_char = datetime.datetime.now() - start_char
                i.update({"userinput": "correct","duration": str(duration_char)})
                print (terminal.green(i["character"] + " = correct in " + i["duration"]))
                typeTutorFunctions.colorizedTypedString(characterlib, (x + 1), showAll=True)
            if k == 'space' and i["character"] == " ":
                duration_char = datetime.datetime.now() - start_char
                i.update({"userinput": "correct","duration": str(duration_char)})
                print (terminal.green(i["character"] + " = correct in " + i["duration"]))
                typeTutorFunctions.colorizedTypedString(characterlib, (x + 1), showAll=True)
            elif k != i["character"]:
                print(terminal.red(k + " = wrong should be " + i["character"]))
                if secondtry == False:
                    i.update({"userinput": "incorrect", "duration": "na"})
                    typeTutorFunctions.colorizedTypedString(characterlib, (x + 1), showAll=True)
                elif secondtry == True:
                    k = typeTutorFunctions.getkey()
                    if k != i["character"]:
                        i.update({"userinput": "incorrect","duration": "na"})
                        print(terminal.red(k + " = still a fail should be " + i["character"]))
                        typeTutorFunctions.colorizedTypedString(characterlib, (x + 1), showAll=True)
                    if k == i["character"]:
                        duration_char = datetime.datetime.now() - start_char
                        i.update({"userinput": "second_try","duration": str(duration_char)})
                        print (terminal.green(i["character"] + " = correct on second try in " + i["duration"]))
                        typeTutorFunctions.colorizedTypedString(characterlib, (x + 1), showAll=True)
        except (KeyboardInterrupt, SystemExit):
            os.system('stty sane')
            print('stopping.')

    print(typeTutorFunctions.summaryResults(characterlib, secondtry))


