def check_int(number):
    try:
        number = int(number)
    except:
        valid = False
    else:
        valid = True
    return number, valid
valid = False
while not valid:
    days = (input("how many days has the car been hired? "))
    days, valid = check_int(days)
    if valid:
        if days >= 1:
            print("accepted")
        else:
            print("must be atleast 1 day")
            valid = False
    else:
        print("must be a number")

valid = False
while not valid:
    start_mileage = input("what was the mileage at the start of the period? ")
    start_mileage, valid = check_int(start_mileage)
    if not valid:
        print("must be a number")

valid = False
while not valid:
    end_mileage = input("what was the mileage at the end of the period? ")
    end_mileage, valid = check_int(end_mileage)
    if not valid:
        print("must be a number")

miles_driven = end_mileage - start_mileage
price = (days * 20) + (miles_driven * 0.05)

print(f"the total cost is £{price}")