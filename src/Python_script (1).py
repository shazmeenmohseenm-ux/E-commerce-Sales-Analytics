import pandas as pd
import os 

folder_path =r"C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\raw"
files = os.listdir(folder_path)
print(files)
 dfs={}

 for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path,file)
        dfs[file] = pd.read_csv(file_path)
        
 print(dfs.keys())  
dfs.keys()
Sales=pd.read_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\raw\ecommerce_sales_customer_analytics_150k.csv')
Sales.head(10)
customer_master=dfs['customer_master.csv']
customer_master.head()
customer_master.shape
customer_master.rename(columns={'customer_postal_code':'Postal_code'},inplace=True)
customer_master.rename(columns={'customer_acquisition_cost':'acquisition_cost'},inplace=True)
customer_master.isnull().sum()
customer_master.duplicated().sum()
dataset_statistics=dfs['dataset_statistics.csv']
dataset_statistics.shape
dataset_statistics.isnull().sum()
dataset_statistics.duplicated().sum()
dataset_statistics.duplicated().sum()
orders=dfs['order_items.csv']
orders.head()
orders.shape
orders.isnull().sum()
orders.duplicated().sum()
products=dfs['product_catalog.csv']
products.head()
products.shape
products.isnull().sum()
products.duplicated().sum()
Sales=dfs['ecommerce_sales_customer_analytics_150k.csv']
Sales.head(10)
Sales.shape
Sales.dtypes
Sales['customer_postal_code'] = Sales['customer_postal_code'].astype(str)
Sales['order_date'] = pd.to_datetime(Sales['order_date'] ,errors='coerce')
Sales['order_time']= pd.to_datetime(Sales['order_time'],errors='coerce')
Sales.select_dtypes(include='number').describe()
Sales.isnull().sum()
Sales.duplicated().sum()
Sales['order_year']=Sales['order_date'].dt.year
Sales['order_month']=Sales['order_date'].dt.month
Sales['order_month_name']=Sales['order_date'].dt.month_name()
Sales['order_day']=Sales['order_date'].dt.day
Sales['order_weekday']=Sales['order_date'].dt.day_name()
age_bins=[17,25,35,45,55,65,75]
age_labels=['17-25','26-35','36-45','46-55','56-65','66-75']
Sales['age_group']=pd.cut(Sales['customer_age'],bins= age_bins,labels =age_labels)
products.to_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\products.csv',index =False)
orders.to_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\orders.csv',index =False)
dataset_statistics.to_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\dataset_statistics.csv',index =False)
customer_master.to_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\customer_master.csv',index =False)
Sales.to_csv(r'C:\Users\Imshu\OneDrive\Pictures\Desktop\PROJECT REPO\E-commerce Sales Analytics\data\sales.csv',index =False)
