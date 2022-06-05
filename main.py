#Calculator by @fcalve4 on GitHub
from math import sqrt
import time

def addition():
    print("Time to add!")
    time.sleep(1)
    print("Input your first number.")
    first = input()
    time.sleep(1)
    print("Input your second number.")
    second = input()
    time.sleep(1)
    answer = float(first) + float(second)
    return answer

def subtraction():
    print("Time to subtract!")
    time.sleep(1)
    print("Input your first number.")
    first = input()
    time.sleep(1)
    print("Input your second number.")
    second = input()
    time.sleep(1)
    answer = float(first) - float(second)
    return answer

def multiplication():
    print("Time to multiply!")
    time.sleep(1)
    print("Input your first number.")
    first = input()
    time.sleep(1)
    print("Input your second number.")
    second = input()
    time.sleep(1)
    answer = float(first) * float(second)
    return answer

def division():
    print("Time to divide!")
    time.sleep(1)
    print("Input your first number.")
    first = input()
    time.sleep(1)
    print("Input your second number.")
    second = input()
    time.sleep(1)
    answer = float(first) / float(second)
    return answer

def average():
    print("How many numbers would you like to average? (integer)")
    count = int(input())
    time.sleep(1)
    lst = []
    for i in range(count):
        print("Please input #" + str(i + 1) + ".")
        lst.append(input())
        time.sleep(1)
    print("Calculating the average of " + str(count) + " numbers.")
    time.sleep(1)
    answer = 0
    for num in lst:
        answer += float(num)
    answer /= count
    return answer

def exponent():
    print("Please select your base number.")
    base = float(input())
    time.sleep(1)
    print("What power would you like to raise " + str(base) + " to?")
    exp = float(input())
    time.sleep(1)
    answer = base ** exp
    return answer

def square_root():
    print("Please input the number you would like to take the root of.")
    num = float(input())
    time.sleep(1)
    answer = sqrt(num)
    return answer

def slope():
    print("Let's find the slope between two points.")
    time.sleep(1)
    print("Input your first 'x' value.")
    x1 = float(input())
    time.sleep(1)
    print("Input your first 'y' value.")
    y1 = float(input())
    time.sleep(1)
    print("Input your second 'x' value.")
    x2 = float(input())
    time.sleep(1)
    print("Input your second 'y' value.")
    y2 = float(input())
    time.sleep(1)
    answer = ((y1 - y2) / (x1 - x2))
    return answer

if __name__ == "__main__":
    answer = []
    print("-Calculator-")
    time.sleep(1)
    while True:
        print("Select an Operation")
        print("'a' for Addition")
        print("'s' for Subtraction")
        print("'m' for Multiplication")
        print("'d' for Division")
        print("'v' for Average")
        print("'e' for Exponent")
        print("'r' for Square Root")
        print("'z' for Slope")
        print("Press 'q' to exit")
        op = input()
        time.sleep(1)
        if op == "a":
            answer = addition()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "s":
            answer = subtraction()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "m":
            answer = multiplication()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "d":
            answer = division()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "v":
            answer = average()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "e":
            answer = exponent()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "r":
            answer = square_root()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "z":
            answer = slope()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "q":
            print("Quitting...")
            time.sleep(1)
            quit()
        else:
            print("Invalid - Try again")
            time.sleep(1)
            continue

