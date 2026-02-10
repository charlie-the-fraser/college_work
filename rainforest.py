import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("amazon_sales_dataset.csv")

total_sales = df["quantity_sold"].sum()
total_revenue = df["total_revenue"].sum()

average_sale = total_revenue / total_sales

print(f"there were {total_sales} total sales that made £{round(average_sale, 2)} average")

categories = list(df["product_category"].drop_duplicates())
category_sales = {}
for i in range(0, len(categories)):
    current_category = df[df["product_category"] == categories[i]]
    category_sales[categories[i]] = current_category["total_revenue"].sum()

plt.bar(category_sales.keys(), [value - 5000000 for value in category_sales.values()] , bottom=5000000)
plt.title("total revenue by category")
plt.xlabel("category")
plt.ylabel("total revenue")
plt.xticks(rotation = 45)
plt.show()

region = df.groupby("customer_region")["total_revenue"].sum()

plt.bar(region.keys(), region.values - 8000000, bottom = 8000000)
plt.title("Revenue by region")
plt.xlabel("region")
plt.ylabel("revenue")
plt.show()