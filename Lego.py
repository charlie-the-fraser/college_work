import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("lego_sets.csv")
print(len(df.columns))
print(len(df))


contains_null = {}
for i in range(0, len(df.columns)):
    column = int(df[df.columns[i]].count())
    if column < len(df):
        contains_null[df.columns[i]] = column

print(contains_null)

mean_price = df["list_price"].mean()
max_price = df["list_price"].max()
print(mean_price, max_price)

x = []
y = []
reader = csv.reader("lego_sets.csv")
for line in reader:
    try:
        int(line["list_price"]) and int(line["piece_count"])
    except:
        valid = False
    else:
        valid = True
        price = int(line["list_price"])
        pieces = int(line["piece_count"])
    if valid:
        x.append(price)
        y.append(pieces)

plt.hist(x)
plt.ylabel("piece count")
plt.xlabel("set price")

plt.show()