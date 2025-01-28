import numpy as np
''' Problem: Sales Data Analysis

You are given monthly sales data for a company's three products across five different regions.
Create a NumPy program to analyze this data and answer specific questions.

Tasks:
Create a 3D array (5 regions × 3 products × 12 months) with random sales data
Calculate total sales per region
Find the best-performing product in each region
Calculate month-over-month growth for each product
Identify the region with the most consistent sales (lowest standard deviation)
Find the peak season (quarter) for each product'''

np.random.seed(42)  # For reproducibility
sales_data = np.random.randint(100, 1000, size=(5, 3, 12))
regions = ['North', 'South', 'East', 'West', 'Central']
products = ['Product A', 'Product B', 'Product C']
print(sales_data)

# Calculate total sales per region
total_sales_per_region = sales_data.sum(axis =(1,2))
print(total_sales_per_region)
#ou bien
for i , j in zip(regions,sales_data):
    print(i,'has a total sales of : ', j.sum ())
#Find the best-performing product in each region

best_performing_product = sales_data.sum(axis =2)
for i, region_sale in enumerate(best_performing_product):
    max_sale = max(region_sale)
    best = list(region_sale).index(max_sale)
    print(f'{regions[i]}:{products[best]}')
    

# to be continued


