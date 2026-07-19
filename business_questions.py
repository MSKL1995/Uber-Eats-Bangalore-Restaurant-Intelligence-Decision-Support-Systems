business_questions = {

"Q1":{

"question":

"Which Bangalore locations have the highest average restaurant ratings?",

"business_value":

"Identifies premium-performing areas suitable for brand positioning and new partner onboarding.",

"sql":

"""
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
"""
},

"Q2":{

"question":

"Which locations are over-saturated with restaurants?",

"business_value":

"Helps avoid overcrowded markets and guides smarter expansion decisions.",

"sql":

"""
SELECT
    location,
    COUNT(DISTINCT name) AS restaurants_offering
FROM restaurants
GROUP BY location
ORDER BY restaurants_offering DESC
LIMIT 15;
"""
},

"Q3":{

"question":

"Does online ordering improve restaurant ratings?",

"business_value":

"Evaluates the ROI of Uber Eats online ordering feature for partner restaurants.",

"sql":

"""
SELECT
    online_order,
    ROUND(AVG(CAST(SUBSTRING_INDEX(rate,'/',1) AS DECIMAL(3,1))), 2) AS average_rating,
    COUNT(DISTINCT name) AS restaurants
FROM restaurants
WHERE rate NOT IN ('NEW','-')
GROUP BY online_order
LIMIT 15;
"""
},

"Q4":{

"question":

"Does table booking correlate with higher customer ratings?",

"business_value":

"Measures whether table booking is associated with higher customer satisfaction.",

"sql":

"""
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
"""
},

"Q5":{

"question":

"What price range delivers the best customer satisfaction?",

"business_value":

"Identifies the pricing segment with the highest average customer ratings.",

"sql":

"""
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
"""
},


"Q6":{

"question":

"How do low, mid and premium-priced restaurants perform?",

"business_value":

"Supports pricing-based market segmentation strategies.",

"sql":

"""
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
"""
},


"Q7":{

"question":

"Which cuisines are most common in Bangalore?",

"business_value":

"Reveals market demand and cuisine saturation levels.",

"sql":

"""
SELECT
    cuisines,
    COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY cuisines
ORDER BY total_restaurants DESC
LIMIT 10;
"""
},

"Q8":{

"question":

"Which cuisines receive the highest average ratings?",

"business_value":

"Identifies high-quality cuisine categories suitable for promotion.",

"sql":

"""
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
"""
},

"Q9": {
    "question":
    "Which restaurant types receive the highest average ratings?",

    "business_value":
    "Helps identify the best-performing restaurant business models.",

    "sql":
    """
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
"""
},

"Q10": {

    "question":
    "Which restaurant types generate the largest restaurant presence?",

    "business_value":
    "Identifies the most competitive business categories.",

    "sql":
    """
SELECT
listed_in_type,
COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY listed_in_type
ORDER BY total_restaurants DESC;
    """
},

"Q11": {

    "question":
    "Which city zones contain the highest number of restaurants?",

    "business_value":
    "Supports regional expansion and delivery planning.",

    "sql":
    """
SELECT
    listed_in_city,
    COUNT(DISTINCT name) AS total_restaurants
FROM restaurants
GROUP BY listed_in_city
ORDER BY total_restaurants DESC
LIMIT 10;
    """
},

"Q12": {

    "question":
    "Which restaurants have received the highest number of customer votes?",

    "business_value":
    "Identifies the most popular restaurants based on customer engagement.",

    "sql":
    """
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
    """
},

"Q13": {

    "question":
    "Which restaurants offer online ordering and table booking together?",

    "business_value":
    "Finds premium restaurants providing multiple customer conveniences.",

    "sql":
    """
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
    """
},

"Q14": {

    "question":
    "Which restaurants charge the highest average cost for two people?",

    "business_value":
    "Identifies premium-priced restaurants in Bangalore.",

    "sql":
    """
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
    """
},

"Q15": {

    "question":
    "Which highly-rated restaurants have the lowest cost for two?",

    "business_value":
    "Finds value-for-money restaurants with excellent customer ratings.",

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
    AND approx_cost_for_two IS NOT NULL
    AND approx_cost_for_two <> ''
GROUP BY
    name,
    location
ORDER BY
    CAST(SUBSTRING_INDEX(MAX(rate), '/', 1) AS DECIMAL(3,1)) DESC,
    CAST(REPLACE(MAX(approx_cost_for_two),',','') AS UNSIGNED) ASC
LIMIT 10;
    """
}


}

