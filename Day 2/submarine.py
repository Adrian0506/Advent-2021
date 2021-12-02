


#DAY 2 advent of coding
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

##Main function that checks for the movement of the submarine
def submarine():
    movement = readFile()
    depth = 0
    horizontal = 0
    aim = 0
    for step in movement:
        if getSubmarineLocation(step) == 'down':
            aim += int(step.split(' ')[1])
        elif getSubmarineLocation(step) == 'up':
            aim -= int(step.split(' ')[1])
        elif getSubmarineLocation(step) == 'forward':
            horizontal += int(step.split(' ')[1])
            if (aim > 0):
              depth += aim * int(step.split(' ')[1])
    print(depth * horizontal)
    return(depth * horizontal)
            


#Quick helper function to determine which step we are currently on and splitting the numbers
def getSubmarineLocation(step):
    currentStep = step.split(' ')
    if currentStep[0] == 'down':
        return 'down'
    elif currentStep[0] == 'forward':
        return 'forward'
    elif currentStep[0] == 'up':
        return 'up'



submarine()


