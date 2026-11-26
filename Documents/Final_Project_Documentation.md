# E-commerce Sales Analytics Project Documentation

## 1\. Project Overview :

This project analyses e-commerce sales, customer behaviour, product performance, marketing activity, operations, returns, and sales trends. It combines Python-based data preparation and machine-learning analysis with Power BI reporting to support data-driven business decisions.

## 2\. Business Problem : 

An e-commerce business generates data across sales transactions, customers, products, orders, marketing channels, delivery, and returns. Reviewing these areas separately can make it difficult to understand overall performance, identify valuable customer groups, recognise return patterns, and plan future sales.

This project brings these areas together for analysis and reporting.

## 3\. Project Objectives :

* Prepare and inspect the supplied e-commerce datasets.
* Analyse sales, customers, products, marketing, delivery, and returns.
* Segment customers using behavioural and purchasing information.
* Build a model to predict whether an order may be returned.
* Explore sales forecasting using time-based features.
* Present business performance through Power BI reports.

## 4\. Dataset Overview :

The project uses five supplied CSV datasets.

|Dataset|Rows|Columns|Purpose|
|-|-:|-:|-|
|`ecommerce\_sales\_customer\_analytics\_150k.csv`|138,116|46|Main sales and customer transaction analysis|
|`customer\_master.csv`|25,000|11|Customer-level information|
|`order\_items.csv`|397,569|12|Order-item details|
|`product\_catalog.csv`|1,175|9|Product information|
|`dataset\_statistics.csv`|1|11|Dataset-level statistical summary|

The detailed field names, data types, descriptions, and data-quality notes are documented in `Data\_Dictionary.md`.

## 5\. Tools and Technologies :

* **Python:** data inspection, preparation, feature engineering, and machine learning
* **Pandas and NumPy:** data manipulation and numerical operations
* **Matplotlib and Seaborn:** data visualisation
* **Scikit-learn:** preprocessing, customer segmentation support, and model evaluation
* **XGBoost:** sales forecasting experiments
* **Jupyter Notebook:** analysis and experimentation
* **Power BI and Power Query:** data modelling, DAX measures, and interactive reporting
* **Git and GitHub:** version control and project hosting

SQL was not used in this project.

## 6\. Data Preparation and Feature Engineering :

The preprocessing workflow includes:

1. Loading the supplied CSV files into Pandas dataframes.
2. Reviewing dataset dimensions, column data types, and sample records.
3. Checking missing values and duplicate records.
4. Renaming selected columns for consistency.
5. Converting order date and order time fields to datetime formats.
6. Creating date-related fields, including order year, month, month name, day, and weekday.
7. Creating customer age groups using age ranges.
8. Exporting prepared datasets for further analysis.

The preprocessing notebook and Python script contain the implementation details. File paths should be configured for the local project folder before running the script on another computer.

## 7\. Customer Segmentation :

Customer segmentation was performed using the K-Means clustering approach and customer purchasing behaviour. The project uses RFM-style behavioural information:

* **Recency:** how recently a customer made a purchase.
* **Frequency:** how often a customer placed orders.
* **Monetary:** the amount spent by a customer.

The work also uses the Elbow Method and Silhouette Score to support the selection and evaluation of the clustering solution. Five clusters (cluster IDs 0–4) are represented in the cluster profile output.

### Cluster profile summary :

The following values are averages from the supplied `cluster\_profile.csv`. Cluster IDs follow the row order in that file.

|Cluster|Avg. orders|Avg. sales|Avg. profit|Avg. return rate|
|-:|-:|-:|-:|-:|
|0|3.60|3,316.48|1,455.20|0.11%|
|1|6.76|8,074.21|3,495.98|5.26%|
|2|4.32|8,497.61|2,533.43|2.71%|
|3|4.36|4,707.45|2,256.96|30.99%|
|4|8.49|14,719.26|5,851.28|7.18%|

Cluster 4 has the highest average order count, sales, and profit in this profile. Cluster 3 has the highest average return rate. These are descriptive observations from the cluster profile; they do not, by themselves, establish the causes of the differences.

## 8\. Order Return Prediction :

A Logistic Regression model was developed to classify whether an order would be returned. The target was created from the order status, with returned orders represented as the positive class.

The final recorded evaluation results are:

|Metric|Result|
|-|-:|
|Accuracy|87.77%|
|Precision|34.90%|
|Recall|90.80%|
|F1-score|50.42%|
|ROC-AUC|94.73%|

### Confusion matrix :

||Predicted not returned|Predicted returned|
|-|-:|-:|
|Actual not returned|22,527|3,205|
|Actual returned|174|1,718|

The model identifies a high proportion of returned orders (recall 90.80%), while its precision is lower (34.90%). This means many orders flagged as likely returns are not actually returned. The model can be considered a screening aid, not a definitive decision-maker. Its predictions should be evaluated alongside the cost of missed returns and unnecessary interventions.

## 9\. Sales Forecasting :

Sales forecasting experiments were carried out using time-based sales data and an XGBoost model. The feature engineering work includes calendar fields, lagged sales values, and rolling sales features.

### Recorded model results :

**Daily forecasting evaluation**

|Metric|Result|
|-|-:|
|MAE|16,616.49|
|RMSE|19,846.05|
|R²|0.5937|
|MAPE|14.26%|

**Monthly forecasting evaluation**

|Metric|Result|
|-|-:|
|MAE|101,029.72|
|RMSE|134,552.43|
|MAPE|3.96%|

A seasonal naive baseline was also considered during the forecasting work and performed better than the monthly XGBoost model. Therefore, XGBoost should not be described as the best-performing forecasting approach based on that comparison. Forecasting model selection should be based on comparison against suitable baselines and performance on chronological holdout data.

## 10\. Power BI Reports:

The project includes the following Power BI report areas:

1. **Executive Overview** – high-level business performance indicators.
2. **Sales \& Profitability Analysis** – sales and profit performance.
3. **Customer Analysis** – customer behaviour and purchasing patterns.
4. **Product Analytics** – product and category performance.
5. **Marketing Analytics** – marketing and sales-channel analysis.
6. **Operations \& Delivery** – operational and delivery performance.
7. **Returns \& Customer Experience** – returns and customer experience analysis.
8. **Customer Segmentation** – customer cluster analysis.
9. **Return Order Prediction** – model results and return-risk analysis.
10. **Sales Forecasting** – historical sales trends and forecast analysis.

The Power BI reports use measures, visuals, and filters to support interactive analysis. The actual report file should be included in the repository only if it is part of the agreed submission and can be shared.

## 11\. Key Observations

* The main sales dataset contains 138,116 records.
* The sales dataset contains 24,911 unique customers.
* There are 9,462 returned orders, representing a return rate of approximately 6.85% in the analysed sales data.
* The customer cluster profile shows differences in average order count, sales, profit, and return rate across the five clusters.
* The return prediction model has high recall but comparatively low precision, so predicted return risk requires careful interpretation.
* The monthly forecasting experiment demonstrates why model results should be compared with a baseline before selecting a forecasting method.

## 12\. Business Recommendations :

* Review the purchasing and profitability patterns of each customer cluster before designing targeted retention or loyalty campaigns.
* Investigate the products, channels, and operational factors associated with higher return rates.
* Use the return prediction model to prioritise further review rather than automatically cancelling or rejecting orders.
* Compare forecasting models with simple baselines and select the model that performs best on out-of-time test data.
* Monitor sales, profitability, delivery, and returns together rather than relying on a single KPI.

These recommendations are suggested actions based on the analyses; they are not claims that the actions have already been implemented or that causation has been established.

## 13\. Project Structure :

A suggested repository structure is:

```text

PROJECT REPO 

&#x20;|

├──  E-commerce Sales Analytics

&#x20;| 

&#x20;|    ├─ Data

&#x20;|

&#x20;|             ├── Raw

&#x20;|                          ├── customer\_master.csv

&#x20;|                          ├── dataset\_statistics.csv 

&#x20;|                          ├──  ecommerce\_sales\_customer\_analytics\_150k.csv

&#x20;|                          ├── order\_items.csv

&#x20;|                          ├── product\_catalog.csv

&#x20;|

&#x20;|             ├── Processed Data

&#x20;|           

&#x20;|                         ├──  customer\_master.csv

&#x20;|                         ├──  dataset\_statistics.csv 

&#x20;|                         ├──  orders.csv

&#x20;|                         ├──   products.csv

&#x20;|                         ├──    Salesdata.csv

&#x20;|  

&#x20;|      ├── src

&#x20;|                ├── Python\_script(1).py

&#x20;|                ├── Data Preprocessing.py 

&#x20;|

&#x20;|

&#x20;|     ├──   Notebook

&#x20;|               ├── Customer Segmentation

&#x20;│              ├── Return prediction

&#x20;|               └── Sales Forecasting 

&#x20;|   



&#x20;|        ├─ Data\_Validation 

&#x20;|                         ├── Data\_Quality\_Report.xlsx 

&#x20;|                         ├── Missing\_Value\_Report.csv 

&#x20;|                         ├── Duplicate\_Report.csv 

&#x20;|                         └── Validation\_Report.md 

&#x20;|      

&#x20;|       

&#x20;|   

&#x20;|         ├── Dashboard

&#x20;|                        ├── e-commerce\_sales\_analytics.pbix 

&#x20;|                        

&#x20;|   

&#x20;|         ├─ Project\_Documentation 

&#x20;|     

&#x20;|                  ├── Data \_Dictionary.md

&#x20;|                  ├──  Project Document

&#x20;|                  ├── Final\_Project\_Documentation.md

&#x20;|        

&#x20;|         ├── README.md

&#x20;|                        └── .gitignore

&#x20;|

&#x20;|        

&#x20;└──          

````
14. Limitations

* Model performance is based on the available dataset and the evaluation approach used in the notebooks.
* The return prediction model's lower precision means some flagged orders will not be returned orders.
* Forecasting performance may vary as sales patterns change over time.
* Cluster profiles describe groups in the available data; business labels and explanations should be validated with domain knowledge.
* Local file paths must be changed before the project can be run on another computer.

## 15\. Conclusion

This project demonstrates an end-to-end analytics workflow using Python, machine learning experiments, and Power BI. It covers data preparation, customer segmentation, return prediction, sales forecasting, and interactive business reporting. The results provide a basis for understanding sales and customer behaviour, identifying return patterns, and evaluating forecasting approaches.

