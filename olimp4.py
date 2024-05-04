import math
number = int(input())

def isIdealNumber(number):
    if number <= 0:
        return False
    number1 = number
    sum = 0
    while number1 > 1:
        number1 = math.ceil(number1 / 2)
        sum = sum + number1
    if sum == number:
        return True
    elif sum != number:
        return False
print(isIdealNumber(number))