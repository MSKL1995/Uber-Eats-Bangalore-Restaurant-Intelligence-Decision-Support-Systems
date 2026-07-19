USE uber_eats;

#Q1
#Question: Which Bangalore locations have the highest average restaurant ratings?

SELECT
    location,
    COUNT(DISTINCT name) AS total_restaurants,
    ROUND(AVG(CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))), 2) AS average_rating
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY location
HAVING COUNT(DISTINCT name) >= 10
ORDER BY average_rating DESC,
         total_restaurants DESC;

#Q2
#Question: Which locations are over-saturated with restaurants?

SELECT
    location,
    COUNT(DISTINCT name) AS restaurants_offering
FROM restaurants
GROUP BY location
ORDER BY restaurants_offering DESC
LIMIT 15;

#Q3
#Question: Does online ordering improve restaurant ratings?

SELECT
    online_order,
    ROUND(AVG(CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))), 2) AS average_rating,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY online_order
LIMIT 15;

#Q4
#Question: Does table booking correlate with higher customer ratings?

SELECT
    book_table,
    ROUND(
        AVG(
            CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))
        ),
        2
    ) AS average_rating,
    COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY book_table
ORDER BY average_rating DESC;

#Q5
#Question: What price range delivers the best customer satisfaction?

SELECT
CASE
WHEN CAST(REPLACE(approx_cost_for_two,',','') AS UNSIGNED) <500
THEN 'Budget'

WHEN CAST(REPLACE(approx_cost_for_two,',','') AS UNSIGNED)
BETWEEN 500 AND 1000
THEN 'Mid Range'

ELSE 'Premium'
END AS price_range,

ROUND(
AVG(
CAST(
SUBSTRING_INDEX(rate,'/',1)
AS DECIMAL(3,1)
)
),
2
) AS average_rating,

COUNT(DISTINCT name) AS restaurants

FROM restaurants

WHERE rate NOT IN ('NEW','-')

GROUP BY price_range

ORDER BY average_rating DESC;


#Q6
#Question: How do low, mid and premium-priced restaurants perform?

SELECT
CASE
    WHEN CAST(REPLACE(approx_cost_for_two, ',', '') AS UNSIGNED) < 500
        THEN 'Budget'

    WHEN CAST(REPLACE(approx_cost_for_two, ',', '') AS UNSIGNED)
         BETWEEN 500 AND 1000
        THEN 'Mid Range'

    ELSE 'Premium'
END AS price_segment,

COUNT(DISTINCT name) AS restaurants,

ROUND(
    AVG(
        CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))
    ),2
) AS average_rating

FROM restaurants

WHERE rate NOT IN ('NEW','-')
AND approx_cost_for_two IS NOT NULL
AND approx_cost_for_two <> ''

GROUP BY price_segment

ORDER BY
CASE price_segment
    WHEN 'Budget' THEN 1
    WHEN 'Mid Range' THEN 2
    WHEN 'Premium' THEN 3
END;

#Q7
#Question: Which cuisines are most common in Bangalore?

SELECT
    cuisines,
    COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY cuisines
ORDER BY total_restaurants DESC
LIMIT 10;


#Q8
# Question: Which cuisines receive the highest average ratings?

SELECT
    cuisines,
    ROUND(AVG(CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))), 2) AS average_rating,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY cuisines
HAVING COUNT(DISTINCT name) >= 5
ORDER BY average_rating DESC
LIMIT 10;


#Q9
# Question: Which restaurant types receive the highest average ratings?

SELECT
    listed_in_type,
    ROUND(
        AVG(CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))),
        2
    ) AS average_rating,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY listed_in_type
ORDER BY average_rating DESC;

#Q10
#Question: Which restaurant types generate the largest restaurant presence?

SELECT
listed_in_type,
COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY listed_in_type
ORDER BY total_restaurants DESC;

#Q11
# Question: Which city zones contain the highest number of restaurants?

SELECT
    listed_in_city,
    COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY listed_in_city
ORDER BY total_restaurants DESC
LIMIT 10;

#Q12
#Question: Which restaurants have received the highest number of customer votes?

SELECT
    name,
    location,
    MAX(votes) AS votes
FROM restaurants
GROUP BY
    name,
    location
ORDER BY votes DESC
LIMIT 10;

#Q13
#Question: Which restaurants offer online ordering and table booking together?

SELECT
    name,
    location,
    MAX(cuisines) AS cuisines,
    MAX(rate) AS rating
FROM restaurants
WHERE
    online_order = 'Yes'
    AND book_table = 'Yes'
    AND rate NOT IN ('NEW', '-')
GROUP BY
    name,
    location
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC
LIMIT 15;

#Q14
# Question: Which restaurants charge the highest average cost for two people?

SELECT
    name,
    location,
    MAX(cuisines) AS cuisines,
    MAX(approx_cost_for_two) AS approx_cost_for_two
FROM restaurants
WHERE
    approx_cost_for_two IS NOT NULL
    AND approx_cost_for_two <> ''
GROUP BY
    name,
    location
ORDER BY
    CAST(REPLACE(MAX(approx_cost_for_two), ',', '') AS UNSIGNED) DESC
LIMIT 10;

# Q15  Which highly-rated restaurants have the lowest cost for two?

SELECT
    name,
    location,
    MAX(cuisines) AS cuisines,
    MAX(rate) AS rating,
    MAX(approx_cost_for_two) AS approx_cost_for_two
FROM restaurants
WHERE
    rate NOT IN ('NEW','-')
    AND approx_cost_for_two IS NOT NULL
    AND approx_cost_for_two <> ''
GROUP BY
    name,
    location
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    CAST(REPLACE(MAX(approx_cost_for_two),',','') AS UNSIGNED) ASC
LIMIT 10;


# Additional Analysis from my end

#Q16
# What is the average order value by payment method?
SELECT
    payment_method,
    ROUND(AVG(order_value),2) AS average_order_value,
    COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY average_order_value DESC;

#Q17
# Which payment methods are used most frequently?
SELECT
    payment_method,
    COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

#Q18
# How frequently are discounts used in customer orders?
SELECT
    discount_used,
    COUNT(*) AS total_orders
FROM orders
GROUP BY discount_used
ORDER BY total_orders DESC;

#Q19
# Which restaurants have received the highest number of orders?
SELECT
    restaurant_name,
    COUNT(*) AS total_orders,
    ROUND(AVG(order_value),2) AS average_order_value
FROM orders
GROUP BY restaurant_name
ORDER BY total_orders DESC
LIMIT 10;

# Q20
# Which locations contain the largest number of highly rated restaurants?
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

#Q21
# What percentage of restaurants provide online ordering?
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

#Q22
# What percentage of restaurants provide table booking?
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

#Q23
# Which cuisine categories have the largest restaurant presence?
SELECT
    cuisines,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
GROUP BY cuisines
HAVING COUNT(DISTINCT name) >= 3
ORDER BY restaurants DESC
LIMIT 20;


#Q24

#Which premium restaurants have excellent ratings?

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
    AND CAST(REPLACE(MAX(approx_cost_for_two),',','') AS UNSIGNED) >= 1000
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    CAST(REPLACE(MAX(approx_cost_for_two), ',', '') AS UNSIGNED) DESC
LIMIT 20;


#Q25
#Which restaurants offer the best combination of high ratings and high customer votes?

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
HAVING
    MAX(votes) >= 100
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    MAX(votes) DESC
LIMIT 20;