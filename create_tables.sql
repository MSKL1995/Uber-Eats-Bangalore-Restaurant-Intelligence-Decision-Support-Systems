USE uber_eats;

CREATE TABLE restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    online_order VARCHAR(10),
    book_table VARCHAR(10),
    rate VARCHAR(20),
    votes INT,
    location VARCHAR(100),
    rest_type TEXT,
    dish_liked TEXT,
    cuisines TEXT,
    approx_cost_for_two VARCHAR(50),
    reviews_list LONGTEXT,
    listed_in_type VARCHAR(100),
    listed_in_city VARCHAR(100)
);

CREATE TABLE orders (
    order_id VARCHAR(100) PRIMARY KEY,
    restaurant_name VARCHAR(255),
    order_date DATE,
    order_value DECIMAL(10,2),
    discount_used VARCHAR(10),
    payment_method VARCHAR(20)
);