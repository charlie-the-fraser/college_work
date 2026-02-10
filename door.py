correct_code = [1, 2, 3, 4]
card = ""
while card == "":
    card = input("Tap your access card ")
    if card == "":
        print("please tap your card")
count = 0
access = False
while count <= 3 and access == False:
    code = []
    for i in range(0, len(correct_code)):
        valid = False
        while valid == False:
            digit = input(f"please enter digit {i + 1} ")
            try:
                int(digit)
            except:
                valid = False
                print("invalid input")
            else:
                digit = int(digit)
                if digit < 0 or digit > 9:
                    valid = False
                    print("invalid input")
                else:
                    valid = True
                    code.append(digit)
    if code == correct_code:
        access = True
    else:
        count += 1
    if count > 3:
        print("door locking, security has been alerted")
    elif not valid:
        print("access denied")
if access:
    if card == "valid":
        print("access granted")
    else:
        print("door locking, security has been alerted")