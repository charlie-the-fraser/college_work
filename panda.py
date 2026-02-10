import pandas as pd
import matplotlib as mp
data = {
    "name" : ["theo", "pihvin", "john"],
    "attendance" : [0, 1, 100],
    "grade" : ["F-", "D", "A+"],
} 


df = pd.DataFrame(data)
df["name"][0] = "penar man"


with open("students.csv", "r", newline="")as file:
    df = pd.read_csv(file)
    
    average = sum(df["Attendance"]) / len(df)
    print(average)
    largerst = df["Attendance"].max()
    lowest = df["Attendance"].min()
    print(largerst, lowest)
    
    below80 = len(df[df["Attendance"] < 80])
    print(below80)

    above90 = len(df[df["Attendance"] >= 90])
    print(above90)

    A = len(df[df["Grade"] == "A"])
    print(f"A ={A}")

    B = len(df[df["Grade"] == "B"])
    print(f"B ={B}")

    C = len(df[df["Grade"] == "C"])
    print(f"C ={C}")

    D = len(df[df["Grade"] == "D"])
    print(f"D ={D}")

    E = len(df[df["Grade"] == "E"])
    print(f"E ={E}")



    at_risk = df[df["Attendance"] <= 80]
    df["At risk"] = "False"
    for i in range(len(df)):
        if df["Attendance"][i] <= 80:
            df["At risk"][i] = "True"
        else:
            df["At risk"][i] = "False"

print(df)
print(at_risk)

df = df.sort_values("Attendance", ascending=False)
print(df)
print(df.head(5))
