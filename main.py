from random import randint
from os import system

 #     Rolling Dice
 #     Version 1.0
 #     Rorounifix@gmail.com
 #     Supported Python Version 2.x


 
 
def dice1():
    print("====================")
    print("||                ||")
    print("||                ||")
    print("||        O       ||")
    print("||                ||")
    print("||                ||")
    print("====================")
    
def dice2():
    print("====================")
    print("||                ||")
    print("||                ||")
    print("||    O      O    ||")
    print("||                ||")
    print("||                ||")
    print("====================")
    
def dice3():
    print("====================")
    print("||                ||")
    print("||                ||")
    print("||    O   O   O   ||")
    print("||                ||")
    print("||                ||")
    print("====================")
    
def dice4():
    print("====================")
    print("||                ||")
    print("||   O       O    ||")
    print("||                ||")
    print("||   O       O    ||")
    print("||                ||")
    print("====================")
    
def dice5():
    print("====================")
    print("||  O          O  ||")
    print("||                ||")
    print("||       O        ||")
    print("||                ||")
    print("||  O          O  ||")
    print("====================")
    
def dice6():
    print("====================")
    print("||   O         O  ||")
    print("||                ||")
    print("||   O         O  ||")
    print("||                ||")
    print("||   O         O  ||")
    print("====================")
    

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
