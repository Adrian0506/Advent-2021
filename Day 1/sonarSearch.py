

def readFile():
    file = open(r"input.txt", "r")
    array = file.read().splitlines()
    desired_array = [int(numeric_string) for numeric_string in array]
    return desired_array

def solve():
    numbers = readFile()
    wordChanges = 0
    previousNumber = 0
    for num in range(len(numbers)):
     try:
       numbers[num + 3]
     except IndexError:
        return wordChanges, 'out of bounds' 
     previousNumber = numbers[num] + numbers[num + 1] + numbers[num + 2]
     nextNumber = numbers[num + 1] + numbers[num + 2] + numbers[num + 3]
     if previousNumber < nextNumber:
      wordChanges += 1
    return wordChanges

solve()