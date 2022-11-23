-- Find the top 3 most frequently bought products
SELECT product_id, SUM(quantity_purchased) AS total_bought
FROM Transactions
GROUP BY product_id
ORDER BY total_bought DESC
LIMIT 3
