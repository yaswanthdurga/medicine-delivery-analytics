-- 1. Total number of orders

SELECT COUNT(*) AS total_orders
FROM medicine_orders;


-- 2. Orders by delivery status

SELECT
    delivery_status,
    COUNT(*) AS order_count
FROM medicine_orders
GROUP BY delivery_status;


-- 3. Average delivery time by city

SELECT
    customer_city,
    ROUND(AVG(delivery_time_hours), 2) AS avg_delivery_hours
FROM medicine_orders
WHERE delivery_status != 'Cancelled'
GROUP BY customer_city
ORDER BY avg_delivery_hours;


-- 4. Revenue by medicine category

SELECT
    category,
    SUM(order_value) AS total_revenue
FROM medicine_orders
WHERE delivery_status != 'Cancelled'
GROUP BY category
ORDER BY total_revenue DESC;


-- 5. Delivery partner performance

SELECT
    delivery_partner,
    COUNT(*) AS total_orders,
    ROUND(AVG(delivery_time_hours), 2) AS avg_delivery_hours
FROM medicine_orders
WHERE delivery_status != 'Cancelled'
GROUP BY delivery_partner
ORDER BY avg_delivery_hours;


-- 6. Delayed orders

SELECT
    order_id,
    medicine,
    customer_city,
    delivery_partner,
    delivery_time_hours
FROM medicine_orders
WHERE delivery_status = 'Delayed'
ORDER BY delivery_time_hours DESC;


-- 7. Highest value medicines

SELECT
    medicine,
    SUM(order_value) AS total_sales
FROM medicine_orders
WHERE delivery_status != 'Cancelled'
GROUP BY medicine
ORDER BY total_sales DESC;