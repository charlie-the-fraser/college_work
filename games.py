import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Game_Shop_Sales_300_Rows.csv")

def most_popular_genre():
    df_2 = df.groupby("Category")["Units Sold"].sum().to_dict()

    plt.pie(df_2.values() , labels= df_2.keys())
    plt.title("most popular genres")
    plt.show()

def game_data():
    df_revenue = df.groupby("Game Title")["Total Revenue (£)"].sum().to_dict()
    df_sales = df.groupby("Game Title")["Units Sold"].sum().to_dict()
    print(df_sales, df_sales)
    plt.subplot(1,2,2)
    plt.bar(df_revenue.keys(), np.round(df_revenue.values()))
    plt.xlabel("game")
    plt.ylabel("Total revenue")
    plt.title("Total revenue per game")
    plt.xticks(rotation = 45)
    plt.subplot(1, 2, 1)
    plt.bar(df_sales.keys(), df_sales.values())
    plt.xlabel("game")
    plt.ylabel("total units sold")
    plt.title("Units sold per game")
    plt.xticks(rotation = 45)
    plt.show()
 
def day_data():
    while True:
        date = input("enter date you want to see 01/01/2024 - 26/10/2024 (DD/MM/YYYY): ")
        try:
            df_date = df[df["Date"] == date]
        except:
            print("you have not entered a valid date")
        else:
            break
    print(df_date)


while True:
    print("1: see most popular genres")
    print("2: see comparison of games sales")
    print("3: do data for specific")
    print("4: quit")
    choice = input("enter choice here: ")
    try:
        choice = int(choice)
    except:
        print("must be an intiger")
    else:
        if choice == 1:
            most_popular_genre()
        elif choice == 2:
            game_data()
        elif choice == 3:
            day_data()
        elif choice == 4:
            print("goodbye")
            break 
        else:
            print("please enter a valid option")