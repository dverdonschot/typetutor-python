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

def charTrainingSet(number, characters):
    """Create a list of characters that the user has to type as training"""
    generated_charTrainingSet = []
    for i in range(number):
        generated_charTrainingSet.append(random.choice(characters))
    return generated_charTrainingSet

def charTrainingSetLib(number, characters):
    """Create a list of characters that the user has to type as training"""
    generated_charTrainingSetLib = {}
    for i in range(number):
        generated_charTrainingSetLib.update({i: {"character": random.choice(characters), "userinput": "", "duration": ""}})
    return generated_charTrainingSetLib

def colorizedTypedString(dictTrainingSet, iteration):
    """Created a colorized string with all typed charaters"""
    import terminal

    for x, i in dictTrainingSet.items():
        if x == (iteration):
            break
        if i["userinput"] == "correct":
            print(terminal.green(i["character"]), end='')
        if i["userinput"] == "incorrect":
            print(terminal.red(i["character"]), end='')
        if i["userinput"] == "second_try":
            print(terminal.blue(i["character"]), end='')
        else:
            print('', end='')
    print("", end="\n")

def summaryResults(dictTrainingSet):
  import datetime
  import statistics
  correct = 0
  second_try = 0
  incorrect = 0
  average_deciseconds_list = []
  for x, i in dictTrainingSet.items():
    if i["userinput"] == 'correct':
      correct = +1
    if i["userinput"] == 'second_try':
      second_try = +1
    if i["userinput"] == 'incorrect':
      incorrect = +1

    timestamp_obj = datetime.datetime.strptime(i["duration"], '%H:%M:%S.%f')
    duration_decisecond = int((timestamp_obj.second * 1000000 + timestamp_obj.microsecond) / 10000)
    average_deciseconds_list.append(duration_decisecond)

  average_duration = int(statistics.mean(average_deciseconds_list)) / 100

  return_var = """##################################################
  Typed First Time Right: {correct}
  Needed a Second Try: {second_try}
  Failed to type correct: {incorrect}
  Average Duration per Typed Character: {average_duration})
  """.format(correct=correct, second_try=second_try, incorrect=incorrect, average_duration=average_duration)

  return return_var
