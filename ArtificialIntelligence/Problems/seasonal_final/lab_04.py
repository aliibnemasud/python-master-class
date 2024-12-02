# Problem 01
import pandas as pd

# Data dictionary
examinee = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'scores': [12.5, 9, 16.5, 2.3, 9, 20, 14.5, 4.5, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualified': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Create a DataFrame
df = pd.DataFrame(examinee)

# Print the "attempts" column
print("Attempts column:")
print(df['attempts'])

# Convert 'qualified' column values into 0’s and 1’s (1 for 'yes', 0 for 'no')
df['qualified'] = df['qualified'].map({'yes': 1, 'no': 0})

# Print the DataFrame after conversion
print("\nDataFrame after converting 'qualified' column values:")
print(df)

# Problem 02
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

