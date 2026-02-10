import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("pixelvault game sales.csv")
def task_one():
    print(df.head())
    print(df.tail())
    print(f"rows = {len(df)}, colums = {len(df.columns)}")

def task_two():
    columns = {}
    for i in range(0, len(df.columns)):
        current_column = df.columns[i]
        columns[current_column] = df.dtypes[i]

    print(columns)

def task_three():
    flag = False
    for i in range(0, len(df)):
        for p in range(0, len(df.columns)):
            if df.isnull()[df.columns[p]][i] == True:
                print(f"oh my god its a null value at row {i} in column {df.columns[p]}")
                flag = True
    if not flag:
        print("there are no null values")
            
    flag = False
    """all_rows = []
    for i in range(0, len(df)):
        for p in range(0, len(all_rows)):
            if str(df.values[i]) in all_rows:
                print(f"duplicate found at row {i}")
                flag = True
        all_rows.append(str(df.values[i]))
        print(f"dont worry, the code is still running, {len(df) - i} left to go")
    if not flag:
        print(f"there are no duplicate rows")
        print(all_rows)"""
    
    duplicateCount = df.duplicated().sum()
    print(df.duplicated)
    print(f"Total Duplicated Values: {duplicateCount}")
    

task_three()