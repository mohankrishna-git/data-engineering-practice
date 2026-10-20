-- Write a query to display all customers from India, sorted alphabetically by customer name.

USE retail_data_engineering;

SELECT *
FROM customers
WHERE country = 'India'
ORDER BY customer_name ASC;