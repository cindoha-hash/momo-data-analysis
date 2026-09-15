-- Show each transaction with its category and related users.
SELECT 
    t.transaction_id,
    t.amount,
    t.transaction_time,
    t.fee,
    t.status,
    tc.category_name,
    sender.name AS sender_name,
    recipient.name AS recipient_name,
    agent.name AS agent_name
FROM Transactions t
JOIN Transaction_Categories tc ON t.category_id = tc.category_id
LEFT JOIN Users sender ON t.sender_id = sender.user_id
LEFT JOIN Users recipient ON t.recipient_id = recipient.user_id
LEFT JOIN Users agent ON t.agent_id = agent.user_id
ORDER BY t.transaction_time DESC;

-- Summarize transaction volume and fees for each category.
SELECT 
    tc.category_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_volume,
    SUM(t.fee) AS total_fees,
    AVG(t.amount) AS avg_transaction_amount
FROM Transactions t
JOIN Transaction_Categories tc ON t.category_id = tc.category_id
GROUP BY tc.category_name
ORDER BY total_volume DESC;

-- Find completed transactions grouped by sender.
SELECT 
    u.name AS sender_name,
    COUNT(t.transaction_id) AS num_transactions,
    SUM(t.amount) AS total_sent
FROM Transactions t
JOIN Users u ON t.sender_id = u.user_id
WHERE t.status = 'completed'
GROUP BY u.name
HAVING SUM(t.amount) > 1000
ORDER BY total_sent DESC;

-- List transactions that failed or were reversed.
SELECT 
    t.transaction_id,
    t.amount,
    t.status,
    t.transaction_time,
    tc.category_name
FROM Transactions t
JOIN Transaction_Categories tc ON t.category_id = tc.category_id
WHERE t.status IN ('failed', 'reversed')
ORDER BY t.transaction_time DESC;

-- Show monthly totals for completed transactions.
SELECT 
    DATE_FORMAT(t.transaction_time, '%Y-%m') AS month,
    COUNT(t.transaction_id) AS transaction_count,
    SUM(t.amount) AS monthly_volume
FROM Transactions t
WHERE t.status = 'completed'
GROUP BY DATE_FORMAT(t.transaction_time, '%Y-%m')
ORDER BY month;

-- Return the details used in a nested transaction response.
SELECT 
    t.transaction_id,
    t.amount,
    t.fee,
    t.new_balance,
    t.transaction_time,
    t.status,
    tc.category_id,
    tc.category_name,
    sender.user_id AS sender_id,
    sender.name AS sender_name,
    sender.phone_number AS sender_phone,
    recipient.user_id AS recipient_id,
    recipient.name AS recipient_name,
    recipient.phone_number AS recipient_phone,
    agent.name AS agent_name
FROM Transactions t
JOIN Transaction_Categories tc ON t.category_id = tc.category_id
LEFT JOIN Users sender ON t.sender_id = sender.user_id
LEFT JOIN Users recipient ON t.recipient_id = recipient.user_id
LEFT JOIN Users agent ON t.agent_id = agent.user_id
WHERE t.transaction_id = 1;