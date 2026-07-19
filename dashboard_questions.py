dashboard_questions = {

    "Restaurant Count": """
        SELECT COUNT(*) AS total
        FROM restaurants;
    """,

    "Order Count": """
        SELECT COUNT(*) AS total
        FROM orders;
    """,

    "Location Count": """
        SELECT COUNT(DISTINCT location) AS total
        FROM restaurants;
    """,

    "Cuisine Count": """
        SELECT COUNT(DISTINCT cuisines) AS total
        FROM restaurants;
    """
}