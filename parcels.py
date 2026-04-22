def get_parcel():
    while True: 
        parcel_num = input("please enter the parcel number: ")
        try:
            int(parcel_num)
        except:
            print("number must consist of intigers only")
        else:
            if len(parcel_num) != 7 :
                print("the number must be 7 characters long")
            else: 
                first_six = list(parcel_num)[0:6]
                seventh_digit = int(list(parcel_num)[6])
                
                total = 0
                for i in range(len(first_six)):
                    total = total + int(first_six[i]) * (i + 1)
                total = total % 10
                if total == seventh_digit: 
                    print("parcel number accepted")
                    break
                else:
                    print("invalid parcel number, are you sure you entered it correctly?")

get_parcel()

        

    