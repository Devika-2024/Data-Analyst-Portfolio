import pandas as pd

# 1. Load the dataset (an Excel or CSV file)
# df = pd.read_csv('sales_data.csv') 

# 2. Check for missing values
# This is a common task to ensure data quality
def check_data(df):
    print("Missing values per column:")
    print(df.isnull().sum())
  
# 3. Clean the data
# If a 'Price' is missing, we fill it with the average price
# df['Price'] = df['Price'].fillna(df['Price'].mean())

# 4. Filter for High Value Users
# This is the 'Both' approach: Code that solves a business problem
def get_pro_users(df):
    pro_users = df[df['Tier'] == 'Pro']
    return pro_users
