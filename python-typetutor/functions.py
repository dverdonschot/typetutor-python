import random
import sys,tty,os,termios

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
        generated_charTrainingSetLib.update({i: {"character": random.choice(characters), "userinput": ""}})
    return generated_charTrainingSetLib
