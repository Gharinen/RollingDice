#!/usr/bin/env python

 #     Rolling Dice
 #     Version 1.0
 #     Rorounifix@gmail.com
 #     Supported Python Version 2.x

from random import randint
from os import *
from pySys import *
from dice import *

if __name__ == "__main__":
    print("My First python Rolling Dice")

def decor():
    print("==================================")
    print("#     Rolling Dice")
    print("#     Version 1.0")
    print("#     Rorounifix@gmail.com")
    print("#     Supported Python Version 2.x")
    print("==================================")

def roll_a_dice():
    x = raw_input("Press 'q' to quit or Enter to Roll a dice : ")
    roll = randint(1,6)
    if(x == 'q'):
        clear()
        print("Good Bye !!!")
    elif(len(x) > 0):
        clear()
        decor()
        print("\n\n\nRoll a dice again!!!\n\n\n")
        roll_a_dice()
    else:
        if(roll == 1):
            clear()
            decor()
            dice1()
            roll_a_dice()
        elif(roll == 2):
            clear()
            decor()
            dice2()
            roll_a_dice()
        elif(roll == 3):
            clear()
            decor()
            dice3()
            roll_a_dice()
        elif(roll == 4):
            clear()
            decor()
            dice4()
            roll_a_dice()
        elif(roll == 5):
            clear()
            decor()
            dice5()
            roll_a_dice()
        elif(roll == 6):
            clear()
            decor()
            dice6()
            roll_a_dice()
        
        
roll_a_dice()
