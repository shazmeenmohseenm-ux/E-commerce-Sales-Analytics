E-Commerce Sales Analytics

1. Project Overview

The E-Commerce Sales Analytics project focuses on analyzing large-scale e-commerce sales, customer, product, and order data to generate meaningful business insights and support data-driven decision-making.

The project involves data extraction, cleaning, transformation, exploratory data analysis, machine learning-based return prediction,customer segmentation,sales forecasting, and interactive Power BI dashboard development.

The objective is to understand business performance, identify customer purchasing patterns, evaluate product performance, analyze return behavior, and forecast future sales trends.

2. Business Problem

E-commerce businesses generate large volumes of transactional data. However, without proper analysis, it becomes difficult to:

Monitor overall sales and profitability.

Understand customer purchasing behavior.

Identify high-performing and underperforming products.

Analyze order returns and customer satisfaction.

Identify customer segments for targeted marketing.

Predict potential product returns.

Forecast future sales performance.

This project addresses these challenges through data analytics, machine learning, and business intelligence techniques.

3. Project Objectives

Analyze overall sales and profitability.

Evaluate customer purchasing patterns and behavior.

Identify top-performing products and categories.

Analyze sales trends across different channels and regions.

Perform customer segmentation using K-Means clustering.

Develop a machine learning model to predict order returns.

Forecast future sales using time-series features and machine learning.

Build interactive Power BI dashboards for business reporting.

Generate actionable insights to support business decisions.

4. Dataset Description

The project uses multiple CSV datasets containing e-commerce transactional and customer information.

Raw Datasets

customer_master.csv

dataset_statistics.csv

ecommerce_sales_customer_analytics_150k.csv

order_items.csv

product_catalog.csv

The datasets contain information about customers, transactions, products, sales channels, payments, shipping, discounts, returns, and order details.

Dataset Highlights

Approximately 150,000 records in the original sales dataset.

138,116 sales records in the processed dataset.

24,911 unique customers.

9,462 returned orders.

6.85% overall return rate.

5. Tools & Technologies

Technology

Purpose

Python

Data analysis and machine learning

Pandas

Data manipulation and cleaning

NumPy

Numerical operations

Matplotlib

Data visualization

Seaborn

Statistical visualization

Power BI

Interactive dashboards and reporting

DAX

Calculated measures and KPIs

Power Query

Data transformation and ETL

Git & GitHub

Version control and project management

Jupyter Notebook

Python development and analysis

6. Project Workflow

Data Collection

Data Understanding

Data Cleaning and Preprocessing

Exploratory Data Analysis (EDA)

ETL Processing

Feature Engineering

Data Modeling

Customer Segmentation

Machine Learning – Return Prediction

Sales Forecasting

Power BI Dashboard Development

Business Insights and Recommendations

7. Data Cleaning and ETL

Python and Power Query were used to prepare the datasets for analysis.

Key activities included:

Handling missing values.

Identifying and removing duplicate records where appropriate.

Correcting data types.

Processing date and time columns.

Handling categorical and numerical variables.

Creating derived columns and analytical features.

Preparing processed datasets for further analysis.

8. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the underlying business patterns.

Key analysis areas:

Sales and revenue distribution.

Order status analysis.

Sales channel performance.

Customer purchasing behavior.

Product and category performance.

Regional sales distribution.

Return order analysis.

Monthly and yearly sales trends.

10. Customer Segmentation – K-Means Clustering

K-Means clustering was implemented to identify different customer groups based on their purchasing behavior.

Key features:

Recency – Time since the customer's last purchase.

Frequency – Number of orders placed.

Monetary – Total customer spending.

The Elbow Method and Silhouette Score were used to support the selection of an appropriate number of clusters.

The resulting customer segments help identify valuable customers and support targeted marketing strategies.

11. Return Order Prediction – Machine Learning

A Logistic Regression classification model was developed to predict whether an order is likely to be returned.

Model Development

Target variable: Return status.

Algorithm: Logistic Regression.

Data preprocessing and categorical encoding.

Training and testing using a train-test split.

Model evaluation using classification metrics.

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

Business Objective

The model aims to identify potentially high-risk return orders so that businesses can investigate return patterns and take preventive actions.

12. Sales Forecasting – XGBoost

Sales forecasting was performed using historical sales data and machine learning techniques.

Feature Engineering

Date-based features.

Day of week.

Month and quarter.

Year.

Lag features (1, 7, 14 and 30 days).

Rolling averages (7-day and 30-day).

Model Development

Algorithm: XGBoost Regressor.

Chronological train-test split.

Daily and monthly sales forecasting.

Evaluation using MAE, RMSE, R² and MAPE.

Monthly Forecasting Performance

Evaluation Metric

Result

MAE

101,029.72

RMSE

134,552.43

MAPE

3.96%

A seasonal naive baseline was also evaluated and performed better than the XGBoost model in the comparison. This highlighted the importance of benchmarking machine learning models against simpler forecasting approaches.

13. Power BI Dashboard Development

Interactive Power BI dashboards were developed to monitor business performance and support decision-making.

Reports Developed

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

KPI cards.

Interactive slicers and filters.

Sales and profitability analysis.

Customer segmentation insights.

Product and category performance.

Regional and channel-wise analysis.

Return analysis and prediction.

Sales forecasting.

DAX measures and calculated metrics.

14. Key Business Insights

The project helps businesses:

Monitor sales and profitability across different channels.

Identify valuable customer segments.

Understand customer purchasing patterns.

Identify products with higher return rates.

Evaluate operational and delivery performance.

Identify potential return risks.

Understand historical sales trends and forecast future demand.

Improve marketing and business strategies using data-driven insights.

15. Project Structure

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
 |      ├── src
 |                ├── Python_script(1).py
 |                ├── Data Preprocessing.py 
 |
 |
 |     ├──   Notebook
 |               ├── Customer Segmentation
 │              ├── Return prediction
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


16. Installation and Execution

Step 1: Clone the Repository

git clone <your-github-repository-url>

Step 2: Navigate to the Project Directory

cd E-commerce-Sales-Analytics

Step 3: Install Required Libraries

pip install pandas numpy matplotlib seaborn scikit-learn xgboost jupyter

Step 4: Run Jupyter Notebook

jupyter notebook

Open the required notebook and execute the cells in sequence.

Note: MySQL and Power BI Desktop can be used separately for SQL analysis and dashboard development.

17. Conclusion

The E-Commerce Sales Analytics project demonstrates an end-to-end data analytics workflow combining Python, SQL, machine learning, forecasting, and Power BI.

It transforms raw e-commerce data into meaningful business insights, helping organizations understand sales performance, customer behavior, product trends, return patterns, and future sales expectations.

The project showcases practical skills in data analytics, data preprocessing, statistical analysis, machine learning, data visualization, and business intelligence.

Project Domain: E-Commerce / Retail Analytics

Project Type: End-to-End Data Analytics Project

Tools: Python | SQL | Power BI | Excel | Git & GitHub
