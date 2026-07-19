# 🍽️ Uber Eats Restaurant Intelligence & Decision Support System

## 📌 Project Overview

This project analyzes Uber Eats Bangalore restaurant and order datasets using **Python**, **MySQL**, **SQL**, and **Streamlit** to generate business insights and support data-driven decision making.

The dashboard allows users to filter restaurants, analyze customer orders, and answer important business questions using SQL queries.

---

## 🎯 Project Objectives

- Clean and preprocess restaurant and order datasets.
- Store cleaned data in MySQL.
- Perform SQL analysis to answer business questions.
- Build an interactive Streamlit dashboard.
- Provide decision-support insights for restaurant businesses.

---

## 🛠 Technologies Used

- Python
- MySQL
- SQL
- Pandas
- SQLAlchemy
- PyMySQL
- Streamlit

---

## 📂 Project Structure

```
Uber_Eats_Project/

├── app.py
├── database.py
├── dashboard_questions.py
├── business_questions.py
├── additional_questions.py
├── data_loading.py
├── load_to_mysql.py
├── create_tables.sql
├── uber_eats.sql
├── project_queries_Updated.sql
├── Uber_Eats_data.csv
├── orders.json
└── README.md
```

---

## 📊 Dashboard Features

### Home Page

- Restaurant Count
- Order Count
- Location Count
- Cuisine Count

---

### Dashboard Filters

Restaurant Filters

- Location
- Cuisine
- Online Order
- Table Booking
- Minimum Rating
- Maximum Cost For Two

Order Filters

- Payment Method
- Discount Used
- Order Value Range

---

## 📈 Business Analysis

The dashboard answers:

- 15 Business Questions
- 10 Additional SQL Questions

using optimized SQL queries.

---

---

## ⚠️ Important Notes

The restaurant dataset stores **multiple cuisines within a single `cuisines` column**. As a result, **Business Question Q3** analyzes the popularity of **cuisine combinations** (for example, *"North Indian, Chinese"* or *"Italian, Pizza"*) instead of individual cuisines. This design decision maintains the integrity of the original dataset and avoids altering the source data during preprocessing.

---

## Business Questions

Examples include:

- Top-rated restaurants
- Restaurants with highest customer votes
- Restaurants offering online ordering and table booking
- Premium restaurants
- Cost analysis
- Customer ratings
- Restaurant popularity

---

## Additional SQL Analysis

Examples include:

- Average order value by payment method
- Most used payment method
- Restaurant order frequency
- Online ordering percentage
- Table booking percentage
- Premium restaurant analysis
- Cuisine popularity

---

## Database

Database Name

```
uber_eats
```

Tables

- restaurants
- orders

---

## How to Run

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

## Output

The application provides

- Interactive Filters
- KPI Dashboard
- Business Insights
- SQL Analysis
- Data Tables

---


## Author

**Kumaravel M**

GUVI – HCL Mini Project


