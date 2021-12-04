


#DAY 3 advent of coding
#In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.


#Reading the file that advent provides us and converting it into a array
def readFile():
    file = open(r"input.txt", "r")
    array = file.read().splitlines()
    return array

##Main function that checks the scrubbing levels and oxygen ratings
def solve(): 
    binaryCodes = readFile()
    mostCommonBit = ''
    leastCommonBit = ''
    currentColumn = 0
    currentNumberArray = []
    currentLength = len(binaryCodes[0])
    while currentColumn < currentLength:
     for code in binaryCodes:
      currentNumberArray.append(code[currentColumn])
     print(currentNumberArray) 
     mostCommonBit += MostCommonBit(currentNumberArray)
     leastCommonBit += LeastCommonBit(currentNumberArray)
     currentNumberArray = []
     currentColumn += 1
    print(int(mostCommonBit, 2) * int(leastCommonBit, 2)) 

def LeastCommonBit(code): 
    ones = 0
    zeros = 0
    for number in code:
        if number == '0':
            zeros += 1
        elif number == '1':
            ones += 1
    if ones < zeros:
        return '1'
    elif zeros < ones: 
        return '0'
 
def MostCommonBit(code):
    ones = 0
    zeros = 0
    for number in code:
        if number == '0':
            zeros += 1
        elif number == '1':
            ones += 1
    if ones > zeros:
        return '1'
    elif zeros > ones: 
        return '0'
solve()