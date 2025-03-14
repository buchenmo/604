import pandas as pd 
from datetime import datetime

# Load CSV files
customers = pd.read_csv('customer.csv')
orders = pd.read_csv('orders.csv')

# Print your name and system details
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"Name: Nick Wang")  # Replace with your name
print(f"Machine Name: {hostname}")
print(f"IP Address: {ip}")

# Merge customer and orders data
merged_data = pd.merge(orders, customers, on='CustomerID')

# Calculate Total Sales
merged_data['TotalSales'] = merged_data['Quantity'] * merged_data['Price']

# Add Status Column
merged_data['Status'] = merged_data['OrderDate'].apply(
    lambda x: 'New' if pd.to_datetime(x) > pd.to_datetime('2024-10-01') else 'Old'
)

# Filter Total Sales > $4500
filtered_data = merged_data[merged_data['TotalSales'] > 4500]

# Save to a new CSV or database table
filtered_data.to_csv('filtered_orders.csv', index=False)

# Print the final aggregated table
print("\nFiltered Orders Table:")
print(filtered_data[['OrderID', 'CustomerName', 'Product', 'TotalSales', 'Status']])