-- Find the top 10 members by spending
SELECT member_id, SUM(cost_dollars * quantity_purchased) AS total_expenditure
FROM Transactions LEFT JOIN Product
  ON Transactions.product_id = Product.product_id
GROUP BY member_id
ORDER BY total_expenditure DESC
LIMIT 10
