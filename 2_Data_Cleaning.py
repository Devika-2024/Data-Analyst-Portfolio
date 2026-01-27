import pandas as pd

# 1. Load the dataset (an Excel or CSV file)
# df = pd.read_csv('sales_data.csv') 
data ={ 'product': ['Paseo','VTT', 'Velo','Paseo',None],
       'Profit' : [100, -50, 75,100,200],
       'Date' : ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-01', '2026-01-03']
      }
df= pd.DataFrame(data)
#2. Remove Duplicates : Essential for Accurate Values
df= df.drop_duplicates()

# 3. Check for missing values
# This is a common task to ensure data quality
def check_data(df):
    print("Missing values per column:")
    print(df.isnull().sum())
  
# 4. Clean the data
# If a 'Price' is missing, we fill it with the average price
  df['Price'] = df['Price'].fillna(df['Price'].mean())

# Filling Missing product names with "unknown'
 df['Product'] = df['Product'].fillna('unknown')

# 5. Filtering : Only show Products with Positive Profit
profitable_products = df[df['Profit']>0]
print(profitable_products)

Filter for High Value Users
# This is the 'Both' approach: Code that solves a business problem
def get_pro_users(df):
    pro_users = df[df['Tier'] == 'Pro']
    return pro_users
