import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Task4a_data_18.csv") 

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show average sales of items within the time period")
        print("3. See comparisons between lunch ad dinner services")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item from the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, start_date, end_date):
    df2 = df[df['Menu Item'] == item].loc[:, start_date : end_date].sum()
    plt.plot(df2.keys(), df2.values)
    plt.title(f"{item} sales over {start_date} - {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation = 45)
    plt.show()
    

def sales_comparison(start_date, end_date):
    items = list(df["Menu Item"])
    df2  = df.loc[:,start_date:end_date]
    item_mean = {}
    item_total = {}
    for i in range(0, len(items)):
        item_mean[items[i]] = df2.values[i].mean()
        item_total[items[i]] = df2.values[i].sum()
    
    plt.subplot(1, 2, 1)
    plt.bar(item_mean.keys(), item_mean.values())
    plt.xlabel("Menu item")
    plt.ylabel("Mean sales")
    plt.xticks(rotation = 45)
    plt.title(f"Mean sales during the period {start_date} - {end_date}")
    plt.subplot(1, 2, 2)
    plt.bar(item_total.keys(), item_total.values())
    plt.xlabel("menu item")
    plt.ylabel("total sales")
    plt.title(f"total sales during the period {start_date} - {end_date}")
    plt.xticks(rotation = 45)
    plt.show()

def lunch_dinner_comparison(start_date, end_date, item):
    lunch = df[df["Service"] == "Lunch"].loc[:,start_date :end_date]
    dinner = df[df["Service"] == "Dinner"].loc[:,start_date : end_date]
    sum_comparison = [lunch.sum().sum(), dinner.sum().sum()]
    labels = ["Lunch", "Dinner"]

    item_comparison = []
    item_lunch = df[df["Menu Item"] == item]
    item_lunch = item_lunch[item_lunch["Service"] == "Lunch"].loc[:,start_date :end_date].sum()
    item_dinner = df[df["Menu Item"] == item]
    item_dinner = item_dinner[item_dinner["Service"] == "Dinner"].loc[:,start_date :end_date].sum()
    print(item_dinner.keys, item_dinner.values)
    plt.subplot(1,2,1)
    plt.plot(item_lunch.keys(), item_lunch.values, label = "Lunch")
    plt.plot(item_dinner.keys(), item_dinner.values, label = "Dinner")
    plt.legend(loc = "upper center")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title(f"lunch and dinner comparison for {item}")
    plt.xticks(rotation = 45)
    plt.subplot(1,2,2)
    plt.pie(sum_comparison, labels=labels)
    plt.title(f"Total sales in period {start_date} - {end_date} for all items")
    plt.show()


main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
    get_selected_item(item, start_date, end_date)
    

elif main_menu == 2:
    start_date = get_start_date()
    end_date = get_end_date()
    sales_comparison(start_date, end_date)

elif main_menu == 3:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
    lunch_dinner_comparison(start_date, end_date, item)
    
else:
    print('This part of the program is still under development')
