-- Find the top 10 members by spending
SELECT member_id, SUM(cost_dollars_per_qty * quantity_purchased) AS total_expenditure
FROM Transactions
GROUP BY member_id
ORDER BY total_expenditure DESC
LIMIT 10
