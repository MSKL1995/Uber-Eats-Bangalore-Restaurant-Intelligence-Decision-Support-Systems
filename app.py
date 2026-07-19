import streamlit as st

from database import run_query
from dashboard_questions import dashboard_questions
from business_questions import business_questions
from additional_questions import additional_questions

st.set_page_config(
    page_title="Uber Eats Dashboard",
    page_icon="🍽️",
    layout="wide"
)

st.sidebar.title("🍽️ Uber Eats Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📋 Dashboard",
        "❓ Business Q&A",
        "📊 Additional Q&A",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":

    st.title("🍽️ Uber Eats Restaurant Intelligence Dashboard")

    st.markdown(
        """
        This dashboard provides business insights into the
        **Uber Eats Bangalore Restaurant Dataset** using
        **Python, MySQL, SQL and Streamlit**.
        """
    )

    restaurant_count = run_query(
    dashboard_questions["Restaurant Count"]
    ).iloc[0]["total"]

    order_count = run_query(
    dashboard_questions["Order Count"]
).iloc[0]["total"]

    location_count = run_query(
    dashboard_questions["Location Count"]
    ).iloc[0]["total"]

    cuisine_count = run_query(
    dashboard_questions["Cuisine Count"]
    ).iloc[0]["total"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🍴 Restaurants",
        f"{restaurant_count:,}"
    )

    col2.metric(
        "🛒 Orders",
        f"{order_count:,}"
    )

    col3.metric(
        "📍 Locations",
        f"{location_count:,}"
    )

    col4.metric(
        "🍕 Cuisines",
        f"{cuisine_count:,}"
    )

    st.divider()

    st.subheader("📌 Project Objective")

    st.info(
        """
        Analyze restaurant performance across Bangalore
        using ratings, pricing, cuisines,
        customer orders and business features
        to support better decision making.
        """
    )

elif page == "📋 Dashboard":

    st.title("📋 Dashboard")

    st.subheader("Restaurant Filters")

    locations = run_query("""
    SELECT DISTINCT location
    FROM restaurants
    ORDER BY location
    """)

    location = st.selectbox(
    "Location",
    ["All"] + locations["location"].tolist()
    )

    cuisines = run_query("""
    SELECT DISTINCT cuisines
    FROM restaurants
    ORDER BY cuisines
    """)

    cuisine = st.selectbox(
    "Cuisine",
    ["All"] + cuisines["cuisines"].tolist()
    )

    online = st.selectbox(
        "Online Order",
        ["All", "Yes", "No"]
    )

    booking = st.selectbox(
        "Table Booking",
        ["All", "Yes", "No"]
    )

    min_rating = st.slider(
        "Minimum Rating",
        0.0,
        5.0,
        3.5,
        0.1
    )

    max_cost = st.slider(
    "Maximum Cost For Two",
    min_value=100,
    max_value=10000,
    value=3000,
    step=100
    )



    if st.button("Apply Restaurant Filter"):

        sql = f"""
        SELECT *
        FROM restaurants
        WHERE
        ('{location}'='All' OR location='{location}')

        AND ('{cuisine}'='All' OR cuisines LIKE '{cuisine}')
        AND (
            '{online}'='All'
            OR online_order='{online}'
        )
        AND (
            '{booking}'='All'
            OR book_table='{booking}'
        )
        AND (
            rate NOT IN ('NEW','-')
        )
        AND (
            CAST(
                SUBSTRING_INDEX(rate,'/',1)
                AS DECIMAL(3,1)
            )>={min_rating}
        )
        AND (
            CAST(
                REPLACE(
                    approx_cost_for_two,
                    ',',
                    ''
                )
                AS UNSIGNED
            )<={max_cost}
        )
        """

        df = run_query(sql)

        st.success(f"{len(df)} Restaurants Found")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    st.subheader("Order Filters")

    payments = run_query("""
    SELECT DISTINCT payment_method
    FROM orders
    ORDER BY payment_method
    """)

    payment = st.selectbox(
        "Payment Method",
        ["All"] + payments["payment_method"].tolist()
    )

    discount = st.selectbox(
        "Discount Used",
        ["All", "Yes", "No"]
    )

    min_order, max_order = st.slider(
        "Order Value",
        min_value=0,
        max_value=10000,
        value=(0, 10000),
        step=100
    )

    if st.button("Apply Order Filter"):

        sql = f"""
        SELECT *
        FROM orders
        WHERE

        (
            '{payment}'='All'
            OR payment_method='{payment}'
        )

        AND

        (
            '{discount}'='All'
            OR discount_used='{discount}'
        )

        AND

        order_value BETWEEN
        {min_order}
        AND
        {max_order}
        """

        df = run_query(sql)

        st.success(f"{len(df)} Orders Found")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

elif page == "❓ Business Q&A":

    st.title("❓ Business Questions")

    questions = {
        business_questions[q]["question"]: q
        for q in business_questions
    }

    selected = st.selectbox(
        "Select Business Question",
        list(questions.keys())
    )

    qid = questions[selected]

    st.info(
        business_questions[qid]["business_value"]
    )

    if st.button("Run Analysis"):

        try:

            df = run_query(
                business_questions[qid]["sql"]
            )

            df.columns = [col.replace("_", " ").title() for col in df.columns]

            st.success(f"{len(df)} results found")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        except Exception as e:

            st.error(e)


elif page == "📊 Additional Q&A":

    st.title("📊 Additional SQL Questions")

    questions = {
        additional_questions[q]["question"]: q
        for q in additional_questions
    }

    selected = st.selectbox(
        "Select Additional Question",
        list(questions.keys())
    )

    qid = questions[selected]

    st.info(
        additional_questions[qid]["business_value"]
    )

    if st.button("Run Analysis"):

        try:

            df = run_query(
                additional_questions[qid]["sql"]
            )

            df.columns = [col.replace("_", " ").title() for col in df.columns]

            st.success(f"{len(df)} results found")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        except Exception as e:

            st.error(e)


elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""
# Uber Eats Restaurant Intelligence & Decision Support System

---

## Project Objective

Develop an interactive Business Intelligence Dashboard using Streamlit, Python, SQL and MySQL to analyze Uber Eats restaurant and order datasets.

---

## Technology Stack

- Python
- Streamlit
- Pandas
- SQLAlchemy
- MySQL
- PyMySQL

---

## Dataset

- Uber Eats Bangalore Restaurant Dataset
- Uber Eats Orders Dataset

---

## Features

- Restaurant Filters
- Order Filters
- 15 Business Questions
- 10 Additional SQL Analyses

---

## Developed By

**Kumaravel M**

GUVI - HCL Capstone Project
""")