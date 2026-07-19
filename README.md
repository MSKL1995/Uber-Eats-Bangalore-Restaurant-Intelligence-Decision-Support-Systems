# Uber-Eats-Bangalore-Restaurant-Intelligence-Decision-Support-Systems

Uber-Eats-Bangalore-Restaurant-Intelligence-Decision-Support-System/
│
├── README.md
├── requirements.txt
├── Uber_Eats_data.csv
├── orders.json
│
├── sql/
│   ├── create_tables.sql
│   ├── uber_eats.sql
│   └── project_queries_Updated.sql
│
├── python/
│   ├── data_loading.py
│   └── load_to_mysql.py
│
└── streamlit/
    ├── app.py
    ├── database.py
    ├── dashboard_questions.py
    ├── business_questions.py
    └── additional_questions.py

--> Important Notes: For Q3 questions, the dataset stores multiple cuisines in a single field, so popularity is measured based on cuisine combinations rather than individual cuisines.

# 🍽️ Uber Eats Restaurant Intelligence & Decision Support System

## 📌 Project Overview

The Uber Eats Restaurant Intelligence & Decision Support System is an interactive Business Intelligence dashboard developed using Python, MySQL, SQL, and Streamlit. The application analyzes restaurant and customer order data to generate meaningful business insights that help restaurants improve customer experience, pricing strategies, and operational decisions.

This project was developed as part of the **GUVI – HCL Capstone Project**.

---

# 🎯 Project Objectives

- Clean and preprocess restaurant and order datasets.
- Store the cleaned data in a MySQL database.
- Perform SQL-based business analysis.
- Build an interactive Streamlit dashboard.
- Answer key business questions using SQL.
- Support data-driven business decision making.

---

# 🗂 Dataset Information

The project uses two datasets:

### Restaurant Dataset

Contains information such as:

- Restaurant Name
- Location
- Cuisine
- Restaurant Type
- Online Ordering
- Table Booking
- Ratings
- Votes
- Approximate Cost for Two
- Listed Category

### Orders Dataset

Contains information such as:

- Order ID
- Restaurant Name
- Order Date
- Order Value
- Payment Method
- Discount Used

---

# 🛠 Technology Stack

- Python
- MySQL
- SQL
- Streamlit
- Pandas
- SQLAlchemy
- PyMySQL

---

# 📂 Project Structure

```
Uber_Eats_Project/

│
├── data/
│ ├── restaurants.csv
│ └── orders.csv
│
├── python/
│ ├── data_loading.py
│ └── load_to_mysql.py
│
├── sql/
│ └── uber_eats.sql
│
├── streamlit/
│ ├── app.py
│ ├── database.py
│ ├── dashboard_questions.py
│ ├── business_questions.py
│ └── additional_questions.py
│
├── README.md
├── requirements.txt
```

---

# ⚙️ Data Cleaning & Preprocessing

The restaurant and order datasets were cleaned using Python.

Cleaning steps included:

- Removing duplicate records
- Handling missing values
- Standardizing column names
- Formatting numeric values
- Preparing data for SQL insertion

---

# 🗄 Database

The cleaned datasets were imported into MySQL.

Database Name:

```
uber_eats
```

Tables:

- restaurants
- orders

---

# 📊 Dashboard Features

## 🏠 Home

Displays:

- Total Restaurants
- Total Orders
- Total Locations
- Total Cuisines

---

## 📋 Dashboard

Restaurant Filters:

- Location
- Cuisine
- Online Order
- Table Booking
- Minimum Rating
- Maximum Cost for Two

Order Filters:

- Payment Method
- Discount Used
- Order Value Range

---

## ❓ Business Questions

The dashboard answers **15 business questions**, including:

- Restaurants by location
- Online ordering analysis
- Restaurant ratings
- Customer votes
- Cost analysis
- Cuisine insights
- Restaurant categories

---

## 📈 Additional SQL Analysis

The application also answers **10 additional SQL questions**, including:

- Payment method analysis
- Average order value
- Discount usage
- Restaurant demand
- Premium restaurants
- Highly rated locations
- Online ordering percentage
- Table booking percentage

---

# 💡 Key Business Insights

The dashboard helps businesses:

- Identify high-performing restaurants
- Analyze customer preferences
- Understand payment behavior
- Compare restaurant categories
- Discover premium restaurant segments
- Support expansion decisions
- Evaluate pricing strategies

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit

```bash
python -m streamlit run streamlit/app.py
```

---

# 🚀 Future Enhancements

- Interactive charts using Plotly
- Download reports to Excel
- Search functionality
- User authentication
- Cloud deployment
- Advanced analytics dashboard

---

# 👨‍💻 Developed By

**Kumaravel M**

GUVI – HCL Capstone Project
