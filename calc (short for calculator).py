import math
def check_int(number):
    try:
        number = int(number)
    except:
        print("invalid")
        valid = False
    else:
        valid = True
    return number, valid

valid = False
while not valid:
    number = input("enter a number: ")
    try:
        number = float(number)
    except:
        print("invalid")
    else:
        valid = True


valid = False
while not valid:
    print("welcome to the calculator!")
    print("1: square number")
    print("2: square root of number")
    print("3: round number")
    print("4: use number as radius of circle to calculate area")
    choice = input("enter choice here: ")
    choice, valid = check_int(choice)
    if valid:
        if choice <= 4 and choice >= 1:
            valid = True
        else:
            valid = False
    if not valid:
        print("invalid input")
if choice == 1:
    answer = number * number
elif choice == 2:
    answer = math.sqrt(number)
elif choice == 3:
    valid = False
    while not valid:
        print("1: round up")
        print("2: round down")
        round_choice = input("enter choice here: ")
        round_choice, valid = check_int(round_choice)
        if valid:
            if round_choice <= 4 and round_choice >= 1:
                valid = True
            else:
                valid = False
        if not valid:
            print("invalid input")
    if round_choice == 1:
        answer = round(math.ceil(number), 2)
    elif round_choice == 2:
        answer = round(math.floor(number), 2)
elif choice == 4:
    answer = math.pi * (number * number)

print(f"the result is {answer}")
