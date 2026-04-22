import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("esp_april_22nd.csv")

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Sales by categories comparison")
        print("3. Product income and profit comparison")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():


    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = df
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))

def get_category():
    while True:
        print("Please choose a product category")
        category = input("Enter category: ")
        if category in df["Category"].unique().tolist():
            return category
        else:
            print("The category you chose is not listed")

def get_data_by_date_and_category(category, start_date, end_date):
    date_ID = df[df["Category"] == category]
    date_ID.loc[start_date : end_date]
    return(date_ID)

def category_sales(date_ID):
    category_df = date_ID
    total_sales = category_df["Qty Sold"].sum()
    total_profit = 0 
    for i in range(0, len(category_df)):
        current_item_sales = category_df["Qty Sold"].tolist()[i]
        total_profit += (current_item_sales * category_df["Sales Price"].tolist()[i]) - (current_item_sales * category_df["Cost Price"].tolist()[i])
    print(f"the total number of sales for the {category} category between {start_date} and {end_date} was {total_sales}")
    print(f"the total profit of the {category} category between {start_date} and {end_date} was £{round(total_profit, 2)}")

def get_data_by_date(start_date, end_date):
    date_df = df.loc[start_date : end_date]
    print(date_df)
    return date_df

def product_comparison(date_df):
    product_codes = df["Product ID"].unique().tolist()
    product_income = []
    product_profit = []
    print(date_df)
    for i in range (0, len(product_codes)):
        current_product = date_df[date_df["Product ID"] == product_codes[i]]
        current_income = float(current_product["Sales Price"].unique()) * current_product["Qty Sold"].sum()
        current_profit = current_income - float(current_product["Cost Price"].unique()) * current_product["Qty Sold"].sum()
        product_income.append(current_income)
        product_profit.append(current_profit)
    plt.subplot(1,2,1)
    plt.bar(product_codes , product_profit)
    plt.title("Product profit")
    plt.xlabel("Products")
    plt.ylabel("Profit")
    plt.subplot(1,2,2)
    plt.pie(product_income, labels=product_codes)
    plt.title("Products income")
    plt.show()

main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)
elif main_menu_choice == 2:
    category = get_category()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_date_and_category(category, start_date, end_date)
    category_sales(date_ID)
elif main_menu_choice == 3:
    start_date = get_date("start")
    end_date = get_date("end")
    date_df = get_data_by_date(start_date, end_date)
    product_comparison(date_df)
