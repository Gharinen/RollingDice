#!/usr/bin/env python

 #     Rolling Dice
 #     Version 1.0
 #     Rorounifix@gmail.com
 #     Supported Python Version 2.x

from random import randint
import os
from pySys import *
from dice import *

if __name__ == "__main__":
    print("My First python")


def roll_a_dice():
    x = raw_input("Press 'q' to quit or Enter to Roll a dice : ")
    roll = randint(1,6)
    if(x == 'q'):
        print("Good Bye !!!")
    elif(len(x) > 0):
        print("Roll a dice again!!!")
        roll_a_dice()
    else:
        if(roll == 1):
            dice1()
            roll_a_dice()
        elif(roll == 2):
            dice2()
            roll_a_dice()
        elif(roll == 3):
            dice3()
            roll_a_dice()
        elif(roll == 4):
            dice4()
            roll_a_dice()
        elif(roll == 5):
            dice5()
            roll_a_dice()
        elif(roll == 6):
            dice6()
            roll_a_dice()
        
        
roll_a_dice()
