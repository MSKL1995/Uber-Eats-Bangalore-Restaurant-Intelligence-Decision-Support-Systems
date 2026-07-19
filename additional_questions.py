additional_questions = {

"Q16": {

    "question":
    "What is the average order value by payment method?",

    "business_value":
    "Helps understand customer spending behavior across different payment methods.",

    "sql":
    """
    SELECT
        payment_method,
        ROUND(AVG(order_value),2) AS average_order_value,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY payment_method
    ORDER BY average_order_value DESC;
    """
},

"Q17": {

    "question":
    "Which payment methods are used most frequently?",

    "business_value":
    "Identifies the most preferred payment options among customers.",

    "sql":
    """
    SELECT
        payment_method,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY payment_method
    ORDER BY total_orders DESC;
    """
},

"Q18": {

    "question":
    "How frequently are discounts used in customer orders?",

    "business_value":
    "Measures customer adoption of promotional discounts and evaluates discount campaign usage.",

    "sql":
    """
SELECT
    discount_used,
    COUNT(*) AS total_orders
FROM orders
GROUP BY discount_used
ORDER BY total_orders DESC;
    """
},

"Q19": {

    "question":
    "Which restaurants have received the highest number of orders?",

    "business_value":
    "Identifies restaurants with the highest customer demand.",

    "sql":
    """
SELECT
    restaurant_name,
    COUNT(*) AS total_orders,
    ROUND(AVG(order_value),2) AS average_order_value
FROM orders
GROUP BY restaurant_name
ORDER BY total_orders DESC
LIMIT 10;
    """
},

"Q20": {

    "question":
    "Which locations contain the largest number of highly rated restaurants?",

    "business_value":
    "Helps identify premium food hubs across Bangalore.",

    "sql":
    """
SELECT
    location,
    COUNT(DISTINCT name) AS highly_rated_restaurants
FROM restaurants
WHERE
    rate NOT IN ('NEW','-')
    AND CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1)) >= 4.0
GROUP BY location
ORDER BY highly_rated_restaurants DESC
LIMIT 10;
    """
},

"Q21": {

    "question":
    "What percentage of restaurants provide online ordering?",

    "business_value":
    "Measures digital adoption among partner restaurants.",

    "sql":
    """
SELECT
    online_order,
    COUNT(*) AS restaurants,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM restaurants),
        2
    ) AS percentage
FROM restaurants
GROUP BY online_order;
    """
},

"Q22": {

    "question":
    "What percentage of restaurants provide table booking?",

    "business_value":
    "Measures customer reservation availability across restaurants.",

    "sql":
    """
SELECT
    book_table,
    COUNT(*) AS restaurants,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM restaurants),
        2
    ) AS percentage
FROM restaurants
GROUP BY book_table;
    """
},

"Q23": {

    "question":
    "Which cuisine categories have the largest restaurant presence?",

    "business_value":
    "Identifies highly competitive cuisine markets.",

    "sql":
    """
SELECT
    cuisines,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
GROUP BY cuisines
HAVING COUNT(DISTINCT name) >= 3
ORDER BY restaurants DESC
LIMIT 20;
    """
},

"Q24": {

    "question":
    "Which premium restaurants have excellent ratings?",

    "business_value":
    "Finds luxury restaurants suitable for premium marketing campaigns.",

    "sql":
    """
SELECT
    name,
    location,
    MAX(cuisines) AS cuisines,
    MAX(rate) AS rating,
    MAX(approx_cost_for_two) AS approx_cost_for_two
FROM restaurants
WHERE
    rate NOT IN ('NEW','-')
GROUP BY
    name,
    location
HAVING
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) >= 4.5
AND
    CAST(REPLACE(MAX(approx_cost_for_two),',','') AS UNSIGNED) >= 1000
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    CAST(REPLACE(MAX(approx_cost_for_two), ',', '') AS UNSIGNED) DESC
LIMIT 20;
    """
},

"Q25": {

    "question":
    "Which restaurants offer the best combination of high ratings and high customer votes?",

    "business_value":
    "Identifies consistently popular restaurants with strong customer satisfaction.",

    "sql":
    """
SELECT
    name,
    location,
    MAX(cuisines) AS cuisines,
    MAX(votes) AS votes,
    MAX(rate) AS rating
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY
    name,
    location
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    HAVING MAX(votes) >= 100
LIMIT 20;
    """
}

}