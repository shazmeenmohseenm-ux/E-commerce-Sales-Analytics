# E-Commerce Sales Analytics – Data Dictionary

## Purpose

This document describes the fields in the five source CSV files supplied for the E-Commerce Sales Analytics project. Data types below reflect the values inferred by pandas when reading the supplied CSV files; date and time fields are currently stored as text in the CSV and may be converted to date/time types during processing.

## Dataset inventory

| Dataset file | Rows | Columns |
|---|---:|---:|
| `ecommerce_sales_customer_analytics_150k(2).csv` | 138,116 | 46 |
| `customer_master(2).csv` | 25,000 | 11 |
| `order_items(2).csv` | 397,569 | 12 |
| `product_catalog(2).csv` | 1,175 | 9 |
| `dataset_statistics(2).csv` | 1 | 11 |

## Relationship and key-field notes

- `customer_master.customer_id` is unique in the customer master file (25,000 distinct IDs).
- `sales.customer_id` contains 24,911 distinct customer IDs and is a natural candidate for linking sales to the customer master.
- `sales.order_id` contains 138,116 distinct IDs in the supplied sales file.
- `order_items.order_id` links line items to orders; the file contains 397,569 rows and 138,116 distinct order IDs.
- `product_catalog.product_id` is unique for all 1,175 product records.
- `order_items.product_id` contains 1,175 distinct product IDs and is a natural candidate for linking order items to the product catalog.
- These are field-based relationship candidates observed from the supplied files. Confirm relationship cardinality and filter direction in the final Power BI/SQL model.

## Field-level dictionary

### Sales Analytics — `ecommerce_sales_customer_analytics_150k(2).csv`

**Dataset size:** 138,116 rows × 46 columns.

| Column | Observed data type | Missing values | Description |
|---|---|---:|---|
| `order_id` | Text / categorical or date-time string | 0 | Unique identifier assigned to an order. |
| `order_date` | Text / categorical or date-time string | 0 | Calendar date on which the order was placed. |
| `order_time` | Text / categorical or date-time string | 0 | Time at which the order was placed. |
| `order_status` | Text / categorical or date-time string | 0 | Current recorded status of the order, such as Completed, Returned, Cancelled or Pending. |
| `sales_channel` | Text / categorical or date-time string | 0 | Channel through which the customer placed the order. |
| `customer_id` | Text / categorical or date-time string | 0 | Identifier linking the order to a customer. |
| `customer_name` | Text / categorical or date-time string | 0 | Recorded customer name associated with the order. |
| `customer_age` | Integer | 0 | Age of the customer at the time represented in the dataset. |
| `gender` | Text / categorical or date-time string | 0 | Recorded gender category of the customer. |
| `customer_segment` | Text / categorical or date-time string | 0 | Business-defined customer segment. |
| `customer_type` | Text / categorical or date-time string | 0 | Customer classification, such as Loyal or other recorded types. |
| `customer_city` | Text / categorical or date-time string | 0 | City associated with the customer. |
| `customer_state` | Text / categorical or date-time string | 0 | State or region-level administrative area associated with the customer. |
| `customer_country` | Text / categorical or date-time string | 0 | Country associated with the customer. |
| `region` | Text / categorical or date-time string | 0 | Business/geographic region assigned to the customer. |
| `customer_postal_code` | Integer | 0 | Postal or ZIP code associated with the customer. |
| `payment_method` | Text / categorical or date-time string | 0 | Payment method used or selected for the order. |
| `payment_status` | Text / categorical or date-time string | 0 | Recorded status of the order payment. |
| `currency` | Text / categorical or date-time string | 0 | Currency code associated with the transaction. |
| `shipping_method` | Text / categorical or date-time string | 0 | Shipping service or delivery option selected. |
| `warehouse` | Text / categorical or date-time string | 0 | Identifier of the warehouse associated with fulfilment. |
| `delivery_days` | Float | 24,557 | Actual delivery duration in days, where available. |
| `estimated_delivery_days` | Float | 24,557 | Estimated delivery duration in days. |
| `delivery_status` | Text / categorical or date-time string | 0 | Recorded delivery performance status, such as On Time. |
| `return_status` | Text / categorical or date-time string | 128,654 | Recorded return status; blank values are present for many records. |
| `return_reason` | Text / categorical or date-time string | 128,654 | Reason recorded for a return, where applicable. |
| `customer_rating` | Float | 24,557 | Customer rating associated with the order or experience. |
| `review_sentiment` | Text / categorical or date-time string | 24,557 | Sentiment category assigned to the customer review. |
| `customer_review` | Text / categorical or date-time string | 24,557 | Text of the customer review, where available. |
| `marketing_channel` | Text / categorical or date-time string | 0 | Marketing channel attributed to the order or customer acquisition. |
| `campaign_name` | Text / categorical or date-time string | 83,233 | Marketing campaign associated with the order, where available. |
| `coupon_code` | Text / categorical or date-time string | 110,502 | Coupon or promotional code applied, where available. |
| `loyalty_points_earned` | Integer | 0 | Number of loyalty points earned. |
| `loyalty_points_redeemed` | Integer | 0 | Number of loyalty points redeemed. |
| `quantity` | Integer | 0 | Total quantity recorded for the order. |
| `gross_sales` | Float | 0 | Sales amount before discounts and other adjustments, as represented in the dataset. |
| `discount_amount` | Float | 0 | Monetary discount applied to the order. |
| `tax_amount` | Float | 0 | Tax amount recorded for the order. |
| `shipping_cost` | Float | 0 | Shipping cost recorded for the order. |
| `net_sales` | Float | 0 | Net sales amount after the applicable sales adjustments represented in the dataset. |
| `product_cost` | Float | 0 | Recorded cost of the products associated with the order. |
| `profit` | Float | 0 | Profit amount recorded for the order. |
| `profit_margin_percentage` | Float | 0 | Profit margin expressed as a percentage. |
| `customer_lifetime_value` | Float | 0 | Recorded customer lifetime value estimate. |
| `is_repeat_customer` | Boolean | 0 | Boolean indicator of whether the customer is identified as a repeat customer. |
| `customer_order_count` | Integer | 0 | Number of orders associated with the customer. |

### Customer Master — `customer_master(2).csv`

**Dataset size:** 25,000 rows × 11 columns.

| Column | Observed data type | Missing values | Description |
|---|---|---:|---|
| `customer_id` | Text / categorical or date-time string | 0 | Unique identifier for a customer; used to link customer records to sales. |
| `customer_name` | Text / categorical or date-time string | 0 | Customer name recorded in the master dataset. |
| `customer_age` | Integer | 0 | Customer age in years. |
| `gender` | Text / categorical or date-time string | 0 | Recorded gender category. |
| `customer_segment` | Text / categorical or date-time string | 0 | Business-defined customer segment. |
| `customer_city` | Text / categorical or date-time string | 0 | Customer city. |
| `customer_state` | Text / categorical or date-time string | 0 | Customer state or administrative area. |
| `customer_country` | Text / categorical or date-time string | 0 | Customer country. |
| `region` | Text / categorical or date-time string | 0 | Geographic/business region assigned to the customer. |
| `customer_postal_code` | Integer | 0 | Customer postal or ZIP code. |
| `customer_acquisition_cost` | Float | 0 | Recorded cost associated with acquiring the customer. |

### Order Items — `order_items(2).csv`

**Dataset size:** 397,569 rows × 12 columns.

| Column | Observed data type | Missing values | Description |
|---|---|---:|---|
| `order_id` | Text / categorical or date-time string | 0 | Identifier of the order to which the line item belongs. |
| `product_id` | Text / categorical or date-time string | 0 | Identifier of the product included in the order. |
| `quantity` | Integer | 0 | Number of units of the product in the line item. |
| `unit_price` | Float | 0 | Price per unit recorded for the product. |
| `discount_percentage` | Float | 0 | Discount rate applied, stored as a numeric fraction in the sample (for example, 0.339607). |
| `discount_amount` | Float | 0 | Monetary discount applied to the line item. |
| `gross_sales` | Float | 0 | Line-item sales amount before discount and other adjustments. |
| `tax_amount` | Float | 0 | Tax amount recorded for the line item. |
| `shipping_cost` | Float | 0 | Shipping cost allocated to the line item. |
| `net_sales` | Float | 0 | Net sales amount recorded for the line item. |
| `product_cost` | Float | 0 | Cost of the product units in the line item. |
| `profit` | Float | 0 | Profit recorded for the line item. |

### Product Catalog — `product_catalog(2).csv`

**Dataset size:** 1,175 rows × 9 columns.

| Column | Observed data type | Missing values | Description |
|---|---|---:|---|
| `product_id` | Text / categorical or date-time string | 0 | Unique identifier for a product. |
| `product_name` | Text / categorical or date-time string | 0 | Name or descriptive title of the product. |
| `product_category` | Text / categorical or date-time string | 0 | Main category to which the product belongs. |
| `product_subcategory` | Text / categorical or date-time string | 0 | More specific product grouping within the category. |
| `brand` | Text / categorical or date-time string | 0 | Brand associated with the product. |
| `supplier` | Text / categorical or date-time string | 0 | Supplier recorded for the product. |
| `unit_price` | Float | 0 | Listed or recorded selling price per unit. |
| `product_cost` | Float | 0 | Recorded cost per product unit. |
| `product_rating` | Float | 0 | Rating associated with the product. |

### Dataset Statistics — `dataset_statistics(2).csv`

**Dataset size:** 1 rows × 11 columns.

| Column | Observed data type | Missing values | Description |
|---|---|---:|---|
| `Total Transactions` | Integer | 0 | Total transaction/order count reported in the summary file. |
| `Total Columns` | Integer | 0 | Number of columns reported for the summarized dataset. |
| `Total Customers` | Integer | 0 | Total customers reported in the summary. |
| `Total Products Used` | Integer | 0 | Total products used/reported in the summary. |
| `Date Range` | Text / categorical or date-time string | 0 | Start and end dates covered by the summarized dataset. |
| `Total Revenue` | Text / categorical or date-time string | 0 | Total revenue value displayed in the summary file. |
| `Total Profit` | Text / categorical or date-time string | 0 | Total profit value displayed in the summary file. |
| `Average Order Value` | Text / categorical or date-time string | 0 | Average order value displayed in the summary file. |
| `Average Rating` | Float | 0 | Average rating displayed in the summary file. |
| `Return Rate` | Text / categorical or date-time string | 0 | Return rate displayed as a percentage in the summary file. |
| `Cancellation Rate` | Text / categorical or date-time string | 0 | Cancellation rate displayed as a percentage in the summary file. |

## Data-quality observations from the supplied files

### Sales Analytics

- The supplied file contains 138,116 rows and 46 columns.
- The following columns contain missing values: `delivery_days` (24,557), `estimated_delivery_days` (24,557), `return_status` (128,654), `return_reason` (128,654), `customer_rating` (24,557), `review_sentiment` (24,557), `customer_review` (24,557), `campaign_name` (83,233), and `coupon_code` (110,502).
- Missing return and review fields may be associated with orders for which no return/review was recorded; confirm the business rule before treating them as data errors.
- `order_date` and `order_time` are read as text from the CSV. Convert them to appropriate date/time types in the analysis workflow when needed.

### Other datasets

- No missing values were detected in the supplied `customer_master.csv`, `order_items.csv`, `product_catalog.csv`, or `dataset_statistics.csv` files.
- `dataset_statistics.csv` is a one-row summary table. Monetary and percentage values in this file are stored as formatted text (for example, `$177,134,263.74` and `6.85%`) rather than numeric values.

## Notes and limitations

- Column descriptions are based on the supplied column names, observed sample values, and common business interpretation. Where a field's exact business rule is not encoded in the CSV, the description is intentionally descriptive rather than asserting an undocumented calculation.
- The data dictionary records the source CSV structure. Any additional columns created during preprocessing, feature engineering, customer segmentation, return prediction, or forecasting should be added in a separate section after inspecting the final processed files and notebook code.
- Numeric values and currencies should be interpreted using the transaction's `currency` field and the project's documented currency-handling rules. Do not assume all transactions share one currency.

---

**Project:** E-Commerce Sales Analytics  
**Document:** Data Dictionary  
**Source:** Five CSV files supplied for the project