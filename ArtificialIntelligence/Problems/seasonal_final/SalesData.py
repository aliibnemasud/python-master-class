import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file into a Pandas DataFrame
df = pd.read_csv('SalesData.csv')

# 2. Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# 3. Calculate the total revenue generated from all sales transactions
total_revenue = df['Revenue'].sum()
print(f"\nTotal revenue generated: {total_revenue}")

# 4. Find the average quantity of products sold per transaction
average_quantity = df['Quantity'].mean()
print(f"\nAverage quantity sold per transaction: {average_quantity}")

# 5. Create a new column named "Month" which extracts the month from the "Date" column
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime format
df['Month'] = df['Date'].dt.month  # Extract the month from the 'Date' column

# 6. Calculate the total revenue generated for each month
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("\nTotal revenue generated for each month:")
print(monthly_revenue)

# 7. Visualize the relationship between quantity sold and revenue using a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['Revenue'], color='blue', alpha=0.5)
plt.title("Relationship between Quantity Sold and Revenue")
plt.xlabel("Quantity Sold")
plt.ylabel("Revenue")
plt.show()
