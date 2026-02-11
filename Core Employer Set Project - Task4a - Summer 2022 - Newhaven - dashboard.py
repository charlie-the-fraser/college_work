import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')

def check_int(number):
    try:
        number = int(number)
    except:
        valid = False
    else:
        valid = True
    return number, valid

def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print("3) increases per region")
    return int(input(""))


def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def region_select():
    region = input("Please enter the name of the region you would like to check: ")
    region = region.capitalize()
    if region in df.Region.values:
        while True:
            print("1) show trends for different property sizes")
            print("2) show trends for all data in the region")
            choice = input("please select an option: ")
            choice, valid = check_int(choice)
            if valid:
                if choice >= 1 and choice <= 2:
                    print("input accepted")
                    break
            print("invalid input")
        while True:
            startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20 ")
            startdate = startdate.capitalize()
            if startdate not in df.columns:
                print("Error start date not found")
            else:
                while True:
                    enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20 ")
                    enddate = enddate.capitalize()
                    if enddate not in df.columns:
                        print("Error end date not found")
                    else:
                        break
                return(region, startdate, enddate, choice)
    else:
        print("Region not found")
    


def region_prices(region_df, start, end, region):
    property_types = list(region_df["Property Type"].drop_duplicates()) 
    property_values = {}
    for i in range(0, len(property_types)):
        current_property = property_types[i]
        current_property_list = region_df[region_df["Property Type"] == current_property]
        property_value = current_property_list.loc[:, start : end].values.mean()
        property_values[current_property] = property_value
    plt.bar(property_values.keys(), property_values.values())
    plt.xlabel("property types")
    plt.ylabel("average price increase")
    plt.title(f"region in the timeframe {start} - {end}")
    plt.xticks(rotation = 45)
    plt.show()




x = mainmenu()
while x == 1 or x == 2 or x == 3:
    if x == 1:
        alldata()

    elif x == 2:
        region, start, end, choice = region_select() 
        region_df = df[df["Region"] == region]
        if choice == 1:
            region_prices(region_df, start, end, region)

    elif x == 3:
        regions = df.groupby("Region")[df.loc[:, "Jan-12" : "May-22"]]
        print(regions)
    x = mainmenu()
