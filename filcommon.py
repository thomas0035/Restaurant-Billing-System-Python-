import pickle
import os

clear = "clear"
pause = "read -p 'Press Enter to Continue...'"

def acceptint(msg, val):
    while True:
        try:
            val = int(input(msg))
            break
        except ValueError:
            print('Invalid Integer Data...')
    return val


def acceptfloat(msg, val):
    while True:
        try:
            val = float(input(msg))
            break
        except ValueError:
            print('Invalid Float Data...')
    return val



def myinp(msg, val):
    if type(val) == int:
        val = acceptint((msg+': '), val)
    if type(val) == float:
        val = acceptfloat((msg+': '), val)
    if type(val) == str:
        val = input(msg+': ')
    return val    
