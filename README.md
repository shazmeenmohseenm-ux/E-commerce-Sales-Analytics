E-Commerce Sales Analytics

Project Overview

The E-Commerce Sales Analytics project is an end-to-end data analytics project focused on analyzing sales, customer behavior, product performance, order returns, and future sales trends.

The project combines Python, Machine Learning, Excel, Power Query, and Power BI to transform raw e-commerce data into meaningful business insights and interactive dashboards.

Business Problem

E-commerce businesses generate large volumes of transactional data. Without proper analysis, it can be difficult to:

Monitor sales and profitability.

Understand customer purchasing behavior.

Identify high-performing products and categories.

Analyze order returns.

Identify valuable customer segments.

Predict potential order returns.

Forecast future sales.

This project addresses these challenges through data analytics, machine learning, and business intelligence.

Project Objectives

Analyze overall sales and profitability.

Understand customer purchasing patterns.

Evaluate product and category performance.

Analyze regional and channel-wise sales.

Perform customer segmentation using K-Means clustering.

Predict order returns using Logistic Regression.

Forecast sales using XGBoost.

Develop interactive Power BI dashboards.

Generate actionable business insights.

Dataset Description

The project uses five raw CSV datasets:

customer_master.csv

dataset_statistics.csv

ecommerce_sales_customer_analytics_150k.csv

order_items.csv

product_catalog.csv

Dataset Highlights

Metric

Value

Original sales records

Approximately 150,000

Processed sales records

138,116

Unique customers

24,911

Returned orders

9,462

Overall return rate

6.85%

Tools and Technologies

Technology

Purpose

Python

Data analysis and machine learning

Pandas

Data cleaning and manipulation

NumPy

Numerical operations

Matplotlib

Data visualization

Seaborn

Statistical visualization

Power BI

Interactive dashboards

DAX

Measures and KPIs

Power Query

Data transformation

Excel

Data validation and analysis

Jupyter Notebook

Python development

Git & GitHub

Version control

Project Workflow

Data Collection

Data Understanding

Data Cleaning and Preprocessing

Exploratory Data Analysis

ETL Processing

Feature Engineering

Customer Segmentation

Machine Learning – Return Prediction

Sales Forecasting

Power BI Dashboard Development

Business Insights and Recommendations

Machine Learning Projects

1. Customer Segmentation – K-Means Clustering

K-Means clustering was implemented to identify customer groups based on purchasing behavior.

Features used:

Recency

Frequency

Monetary Value

The Elbow Method and Silhouette Score were used to support cluster selection.

Business Objective: Identify valuable customer groups and support targeted marketing strategies.

2. Return Order Prediction – Logistic Regression

A Logistic Regression classification model was developed to predict whether an order is likely to be returned.

Model Performance

Evaluation Metric

Result

Accuracy

87.75%

Precision

34.88%

Recall

90.96%

F1-Score

50.42%

ROC-AUC

94.71%

Business Objective: Identify potentially high-risk return orders and help businesses investigate return patterns.

3. Sales Forecasting – XGBoost

Sales forecasting was performed using historical sales data and engineered time-series features.

Features included:

Day of week

Day of month

Month

Quarter

Year

Lag features (1, 7, 14 and 30 days)

Rolling averages (7-day and 30-day)

Monthly Forecasting Performance

Evaluation Metric

Result

MAE

101,029.72

RMSE

134,552.43

MAPE

3.96%

A seasonal naïve baseline was also evaluated and performed better than XGBoost in the comparison. This demonstrated the importance of benchmarking machine learning models against simpler forecasting methods.

Power BI Dashboard Development

Ten interactive reports were developed:

Executive Overview

Sales & Profitability Analysis

Customer Analysis

Product Analytics

Marketing Analytics

Operations & Delivery

Returns & Customer Experience

Customer Segmentation

Return Order Prediction

Sales Forecasting

Dashboard Features

KPI cards

Interactive slicers and filters

Sales and profitability analysis

Customer segmentation insights

Product and category performance

Regional and channel-wise analysis

Return analysis and prediction

Sales forecasting

DAX measures and calculated metrics

Key Business Insights

The project supports businesses in:

Monitoring sales and profitability.

Identifying valuable customer segments.

Understanding customer purchasing patterns.

Identifying products with higher return rates.

Evaluating delivery and operational performance.

Identifying potential return risks.

Understanding historical sales trends and future demand.

Repository Structure

PROJECT REPO 
 |
 ├──  E-commerce Sales Analytics
 | 
 |    ├─ Data
 |
 |             ├── Raw
 |                          ├── customer_master.csv
 |                          ├── dataset_statistics.csv 
 |                          ├──  ecommerce_sales_customer_analytics_150k.csv
 |                          ├── order_items.csv
 |                          ├── product_catalog.csv
 |
 |             ├── Processed Data
 |           
 |                         ├──  customer_master.csv
 |                         ├──  dataset_statistics.csv 
 |                         ├──  orders.csv
 |                         ├──   products.csv
 |                         ├──    Salesdata.csv
 |  
 |         ├── src
 |                ├── Python_script(1).py
 |                ├── Data Preprocessing.py 
 |
 |
 |     ├──   Notebook
 |               ├── Customer Segmentation
 │               ├── Return prediction
 |               └── Sales Forecasting 
 |   

 |        ├─ Data_Validation 
 |                         ├── Data_Quality_Report.xlsx 
 |                         ├── Missing_Value_Report.csv 
 |                         ├── Duplicate_Report.csv 
 |                         └── Validation_Report.md 
 |      
 |       
 |   
 |         ├── Dashboard
 |                        ├── e-commerce_sales_analytics.pbix 
 |                        
 |   
 |         ├─ Project_Documentation 
 |     
 |                  ├── Data _Dictionary.md
 |                  ├──  Project Document 
 |                  ├── Final_Project_Documentation.md
 |        
 |         ├── README.md
 |                        └── .gitignore
 |
 |        
 └──          

Installation and Execution

Step 1: Clone the Repository

git clone https://github.com/shazmeenmohseenm-ux/E-commerce-Sales-Analytics.git

Step 2: Navigate to the Project Directory

cd E-commerce-Sales-Analytics

Step 3: Install Required Libraries

pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter

Step 4: Launch Jupyter Notebook

jupyter notebook

Open the required notebook and execute the cells in sequence.

Note: Power BI Desktop is required to open and explore the .pbix dashboard file.

Conclusion

This project demonstrates an end-to-end data analytics workflow using Python, machine learning, and Power BI.

It transforms raw e-commerce data into meaningful insights that help understand sales performance, customer behavior, product trends, return patterns, and future sales expectations.

Project Domain: E-Commerce / Retail Analytics

Project Type: End-to-End Data Analytics Project
