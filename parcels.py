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
                break
        first_six = list(parcel_num)[0:6]
        seventh_digit = list(parcel_num)[6]
        

    