import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WinterSD.csv")

years = {}
feminism = {}
for i in range(len(df)):
    current_year = int(df["Year"][i])
    if df["Gender"][i] == "Women":
        flag = True
    else:
        flag = False
    if  current_year not in years.keys():
        years[current_year] = 1
    else:   
        years[current_year] += 1
    if flag:
        if current_year not in feminism.keys():
            feminism[current_year] = 1
        else:
              feminism[current_year] += 1
    
for index, number in enumerate(feminism):
    feminism[index] = (number / years[index]) * 100

plt.plot(feminism.keys(), feminism.values())
plt.xlabel("years")
plt.ylabel("women (%)")
plt.title("feminism")
plt.show()
    
        