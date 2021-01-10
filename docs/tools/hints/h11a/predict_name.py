#!/usr/bin/env python3
import sys
from mt19937 import mt19937, untemper

if __name__ == "__main__":
    # Read discarded numbers from random.txt
    file = open('random.txt', 'r') 
    numbers = file.readlines() 
    numbers = [(int)(x.strip()) for x in numbers]

    # create an MT19937 PRNG
    myprng = mt19937(0)

    # clone the Snowball Fight PRNG
    for i in range(len(numbers)):
        myprng.MT[i] = untemper(numbers[i])

    # predict the player name
    print(f'Your name is: {myprng.extract_number()}')
