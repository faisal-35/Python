
import numpy as np

# Generate random sales data
sales = np.random.randint(100, 500, (3, 4))
print("Sales data (rows=products, columns=quarters):\n", sales)

# Calculate total sales per product
total_sales_per_product = np.sum(sales, axis=1)
print("Total sales per product:\n", total_sales_per_product)

# Calculate average sales per quarter
average_sales_per_quarter = np.mean(sales, axis=0)
print("Average sales per quarter:\n", average_sales_per_quarter)

# Find the best quarter per product
best_quarter_per_product = np.argmax(sales, axis=1)
print("Best quarter per product (0=Q1, 1=Q2, 2=Q3, 3=Q4):\n", best_quarter_per_product)
