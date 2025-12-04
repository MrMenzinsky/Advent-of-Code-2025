import os
import functools
import math

os.chdir('c:/Privat/Anton/Advent_of_Code_2025/Day_01/')

with open('Part_1_input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

def parseData(step):
    if (step[0] == 'L'):
        return 0 - int(step[1:])
    elif (step[0] == 'R'):
        return int(step[1:])
    else:
        raise "Error! Data: "+step

rotations = list(map(parseData, data))

countZeros = 0

def traverse(position, rotation):
    global countZeros
    newPosition = position + rotation
    if (newPosition == 0):
        countZeros += 1
        return 0
    elif (newPosition > 99):
        countZeros = countZeros + math.floor(newPosition / 100)
        newPosition = newPosition % 100
        return newPosition
    elif (newPosition < 0):
        countZeros = countZeros + 1 if position != 0 else countZeros
        countZeros = countZeros + abs(math.ceil(newPosition / 100))
        newPosition = (newPosition + 10000) % 100
        return newPosition
    else:
        return newPosition

functools.reduce(traverse, rotations, 50)
print("Nr of stops at 0: "+ str(countZeros))

# functools.reduce(traverse, [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82], 50)
# print("Nr of stops at 0: "+ str(countZeros))
