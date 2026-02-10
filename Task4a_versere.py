import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Task4a_data_1.csv")
def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Versere Cars Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

def total_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Total Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice      

def convert_total_menu_coice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "All"
    else:
        total_choice = "Model"  
    
    return total_choice

def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data_1.csv")

    if total_choice == "All":
        extract = df.groupby(['Date','Car Model'], sort=True)['Value'].sum()
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    else:
        flag = True

        while flag:

            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            
            choice = input('Enter your number selection here: ')

            try:
                int(choice)
            except:
                print("Sorry, you did not enter a valid option")
                flag = True
            else:    
                print('Choice accepted!')
                choice = int(choice)
                flag = False

        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   

        custom_choice = models[choice -1]

        extract = df.loc[df['Car Model'] == custom_choice]
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    

    return extract

def sales_choice():
    flag = True
    while flag:
        print("###### Please select an option ######")
        print("### 1. See sales over time for salespeople ###")
        print("### 2. See sales over time for new and used cars ###")
        choice = input("Enter choice here: ")
        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else: 
            if int(choice) <= 2 and int(choice) >= 1:   
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")
                flag = True
    return choice

def sales_data(choice, df):
    if choice == "1":
        salespersons = {}
        for i in range(0, len(df)):
            current_salesperson = df["Salesperson"][i]
            if current_salesperson not in salespersons:
                salespersons[current_salesperson] = 1
            else:
                salespersons[current_salesperson] += 1
        plt.bar(salespersons.keys(), salespersons.values())
        plt.xlabel("sales person")
        plt.ylabel("number of sales")
        plt.show()
    elif choice == "2":
        used_sales = {"Used" : 0 , "New" : 0}
        used_total = sum(df[df["New/Used"] == "Used"]["Value"])
        new_total = sum(df[df["New/Used"] == "New"]["Value"])
        for i in range(0, len(df)):
            if df["New/Used"][i] == "New":
                used_sales["New"] += 1
            else:
                used_sales["Used"] += 1
        print(used_total, new_total)
        plt.pie(used_sales.values(), labels=used_sales.keys())
        plt.title(f"total sales are {sum(used_sales.values())}")
        plt.subplot(1, 2, 1)
        plt.bar(["Used", "New"], [used_total, new_total])
        plt.show()
        
        


main_menu_choice = main_menu()

if main_menu_choice == "1":
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_coice(total_menu_choice)
    print(get_total_data(total_choice))
elif main_menu_choice == "2":
    sale_data_choice = sales_choice()
    sales_data(sale_data_choice, df)
    
