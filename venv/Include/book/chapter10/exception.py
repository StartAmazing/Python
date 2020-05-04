try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("------------------- try-except-else -------------------")
print("Give me two numbers,and I'll divide them: ")
print("Enter 'q' to quit. ")

while False:
    firstNum = input("\nFirst Number: ")
    secondNum = input("\nSecond Number: ")
    if firstNum == 'q' or secondNum == 'q':
        break

    try:
        res = int(firstNum) / int(secondNum)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("firstNum or secondNum you get is not a number!")
    else:
        print(res)

print("-------------------- file not found ------------------")
file_name="alice.txt"
try:
    with open(file_name) as file_obj:
        print(file_obj)
except FileNotFoundError:
    print("Sorry, we cannot found the file you applied. ")