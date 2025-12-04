import os
import functools

os.chdir('c:/Privat/Anton/Advent_of_Code_2025/Day_01/')

with open('Part_1_input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

def parseData(step):
    # print(step)
    if (step[0] == 'L'):
        return 0 - int(step[1:])
    elif (step[0] == 'R'):
        return int(step[1:])
    else:
        raise "Error! Data: "+step

rotations = list(map(parseData, data))
# print(rotations)

# dial = list(range(0,100,1))
countZeros = 0

def traverse(rotation, position):
    global countZeros
    newPosition = position + rotation
    if (newPosition == 0 or newPosition == 100):
        countZeros += 1
        return 0
    elif (newPosition > 100):
        newPosition = newPosition % 100
        countZeros = countZeros + 1 if newPosition == 0 else countZeros
        return newPosition
    elif (newPosition < 0):
        newPosition = (newPosition + 10000) % 100
        countZeros = countZeros + 1 if newPosition == 0 else countZeros
        return newPosition
    else:
        return newPosition

functools.reduce(traverse, rotations, 50)

print("Nr of stops at 0: "+ str(countZeros))