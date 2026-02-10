import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Regional statistics")
        print("### 3. Sales over time")
        print("### 4. Leave")

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

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

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

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg

def region_menu():
    regions = pd.read_csv("Task4a_data.csv")
    regionlist = []
    for i in range(0, len(regions)):
        current_region = regions.loc[i]["Region"]
        if current_region not in regionlist:
            regionlist.append(current_region)
    valid = False
    while not valid:
        selection = input("which region would you like to see the statistics for? ")
        if selection in regionlist:
            print("choice accepted!")
            valid = True
        else:
            print("invalid choice")
            flag = True
            while flag:
                print("###### please select an option ######")
                print("### 1. view all available regions ###")
                print("### 2. re-enter region choice ###")
                print("### 3. go back to main menu ###")
                choice = input("Enter your selection here: ")
                try:
                    int(choice)
                except:
                    print("Sorry, you did not enter a valid option")
                    flag = True
                else:
                    if int(choice) >= 1 and int(choice) <= 3:    
                        print('Choice accepted!')
                        choice = int(choice)
                        flag = False
                    else:
                        print("Sorry, you did not enter a valid option")
                        flag = True
            if choice == 1:
                print(f"the available regions are: {regionlist}")
            elif choice == 3:
                return "fail"
    return selection

def region_data(chosen_region):
    file = pd.read_csv("Task4a_data.csv")
    chosen_region_data = file[file["Region"] == chosen_region]
    loop = True
    while loop:
        flag = True
        while flag:
            print("###### please select an option ######")
            print("### 1. see graph of issue types in region ###")
            print("### 2. see graph of resolutions in region ###")
            print("### 3. see average No of parcels in region ###")
            print("### 4. see average days to resolve in region ###")
            print("### 5. see all data for region ###")
            print("### 6. return to main menu ###")
            choice = input("Enter choice here: ")
            try:
                int(choice)
            except:
                print("Sorry, you did not enter a valid option")
                flag = True
            else: 
                if int(choice) <= 6 and int(choice) >= 1:   
                    print('Choice accepted!')
                    flag = False
                else:
                    print("Sorry, you did not enter a valid option")
                    flag = True
        if choice == "1":
            region_issue_types = {}
            for i in range(0, len(chosen_region_data)):
                current = chosen_region_data.iloc[i]["Issue Type"]
                if current not in region_issue_types:
                    region_issue_types[current] = 1
                else:
                    region_issue_types[current] += 1
            plt.pie(region_issue_types.values(), labels=region_issue_types.keys())
            plt.title(f"Issue Types in {chosen_region}")    
            plt.show()
        elif choice == "2":
            region_resolution = {}
            for i in range(0, len(chosen_region_data)):
                current = chosen_region_data.iloc[i]["How Resolved"]
                if current not in region_resolution:
                    region_resolution[current] = 1
                else:
                    region_resolution[current] += 1
            plt.pie(region_resolution.values(), labels=region_resolution.keys())
            plt.title(f"Resolutions in {chosen_region}")    
            plt.show()
        elif choice == "3":
            average_parcels = sum(chosen_region_data["No Of Parcels"]) / len(chosen_region_data)
            print(f"the average number of parcels is {average_parcels}")
        elif choice == "4":
            average_days = sum(chosen_region_data["Days To Resolve"]) / len(chosen_region_data)
            print(f"the average number of days to resolve is {average_days}")
        elif choice == "5":
            print(chosen_region_data)
        elif choice == "6":
            return
    


main_menu_choice = "0"
while main_menu_choice != "3":
    main_menu_choice = main_menu()
    if main_menu_choice ==  "1":
        total_menu_choice = total_menu()
        print(get_total_data(total_menu_choice))
    elif main_menu_choice == "2":
        chosen_region = region_menu()
        if chosen_region != "fail":
            region_data(chosen_region)
    elif main_menu_choice == "4":
        print("##### goodbye! #####")
