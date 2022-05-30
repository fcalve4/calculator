#Calculator by @fcalve4 on GitHub
import time
def addition():
    print("Input your first number. (integer)")
    first = input()
    time.sleep(1)
    print("Input your second number. (integer)")
    second = input()
    time.sleep(1)
    answer = int(first) + int(second)
    return answer

def subtraction():
    print("Input your first number. (integer)")
    first = input()
    time.sleep(1)
    print("Input your second number. (integer)")
    second = input()
    time.sleep(1)
    answer = int(first) - int(second)
    return answer

def multiplication():
    print("Input your first number. (integer)")
    first = input()
    time.sleep(1)
    print("Input your second number. (integer)")
    second = input()
    time.sleep(1)
    answer = int(first) * int(second)
    return answer
def division():
    print("Input your first number. (integer)")
    first = input()
    time.sleep(1)
    print("Input your second number. (integer)")
    second = input()
    time.sleep(1)
    answer = int(first) / int(second)
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
        answer += int(num)
    answer /= count
    return answer

def exponent():
    print("Please select your base number. (integer)")
    base = int(input())
    time.sleep(1)
    print("What power would you like to raise " + str(base) + " to?")
    exp = int(input())
    time.sleep(1)
    answer = base ** exp
    return answer

if __name__ == "__main__":
    answer = []
    print("-Calculator-")
    time.sleep(1)
    while True:
        print("Select an Operation\n'a' for Addition\n's' for Subtraction\n'm' for Multiplication\n'd' for Division\n'v' for Average\n'e' for Exponent\nPress 'q' to exit")
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
        elif op == "avg":
            answer = average()
            print("The answer is: " + str(answer) + ".")
            break
        elif op == "e":
            answer = exponent()
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

