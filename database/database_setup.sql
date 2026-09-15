-- ---------- USERS ----------
CREATE TABLE Users (
    user_id         INTEGER         PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(100)    NOT NULL COMMENT 'Display name of the customer, recipient, source, or agent.',
    phone_number    VARCHAR(20)     NULL COMMENT 'Normalized phone number when available.',
    account_number  VARCHAR(30)     NULL COMMENT 'Mobile money account identifier when available.',
    type            ENUM('self','individual','deposit_source','agent') NOT NULL COMMENT 'Role of the party in the transaction data.',
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_users_phone (phone_number),
    UNIQUE KEY uq_users_account (account_number)
) COMMENT = 'People and entities that appear as a party to a transaction: the account holder, named recipients, deposit sources, and agents.';


-- ---------- TRANSACTION_CATEGORIES ----------
CREATE TABLE Transaction_Categories (
    category_id     INTEGER         PRIMARY KEY AUTO_INCREMENT,
    category_name   ENUM('payment','transfer','deposit','withdrawal','airtime','data_bundle','other') NOT NULL,
    description     VARCHAR(255)    NULL COMMENT 'Human-readable explanation of the category.',
    UNIQUE KEY uq_category_name (category_name)
) COMMENT = 'Lookup table for what kind of transaction an event is. One category, many transactions.';


-- ---------- TRANSACTIONS ----------
CREATE TABLE Transactions (
    transaction_id           INTEGER         PRIMARY KEY AUTO_INCREMENT,
    amount                   DECIMAL(15,2)   NOT NULL COMMENT 'Transaction amount in Rwandan francs.',
    transaction_time         DATETIME        NOT NULL COMMENT 'Date and time extracted from the SMS.',
    fee                      DECIMAL(15,2)   NULL COMMENT 'Fee charged for the transaction.',
    new_balance              DECIMAL(15,2)   NULL COMMENT 'Account balance after the transaction.',
    tx_id                    VARCHAR(50)     NULL,
    financial_transaction_id VARCHAR(50)     NULL,
    external_transaction_id  VARCHAR(50)     NULL,
    status                   ENUM('completed','failed','reversed') NOT NULL DEFAULT 'completed',
    category_id              INTEGER         NOT NULL,
    sender_id                INTEGER         NULL,
    recipient_id             INTEGER         NULL,
    agent_id                 INTEGER         NULL,
    CHECK (amount >= 0),
    CHECK (fee IS NULL OR fee >= 0),
    CHECK (new_balance IS NULL OR new_balance >= 0),
    UNIQUE KEY uq_transactions_tx_id (tx_id),
    CONSTRAINT fk_transactions_category FOREIGN KEY (category_id) REFERENCES Transaction_Categories(category_id),
    CONSTRAINT fk_transactions_sender FOREIGN KEY (sender_id) REFERENCES Users(user_id),
    CONSTRAINT fk_transactions_recipient FOREIGN KEY (recipient_id) REFERENCES Users(user_id),
    CONSTRAINT fk_transactions_agent FOREIGN KEY (agent_id) REFERENCES Users(user_id)
) COMMENT = 'One row per transaction event. Holds everything specific to a single event; parties are referenced by FK to Users.';


-- ---------- TRANSACTION_PARTIES (M:N junction) ----------
CREATE TABLE Transaction_Parties (
    transaction_id  INTEGER      NOT NULL,
    user_id         INTEGER      NOT NULL,
    party_role      ENUM('sender','recipient','agent','other') NOT NULL,
    PRIMARY KEY (transaction_id, user_id, party_role),
    CONSTRAINT fk_party_transaction FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id) ON DELETE CASCADE,
    CONSTRAINT fk_party_user FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
) COMMENT = 'Junction table allowing a transaction to involve multiple users in different roles.';


-- ---------- SYSTEM_LOGS ----------
CREATE TABLE System_Logs (
    log_id          INTEGER         PRIMARY KEY AUTO_INCREMENT,
    process_name    VARCHAR(100)    NOT NULL COMMENT 'ETL or API process that produced the log.',
    log_level       ENUM('INFO','WARNING','ERROR') NOT NULL,
    message         VARCHAR(500)    NOT NULL COMMENT 'Human-readable processing result or error.',
    records_affected INTEGER        NOT NULL DEFAULT 0,
    logged_at       DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (records_affected >= 0)
) COMMENT = 'Audit trail for parsing, cleaning, categorization, loading, and API operations.';


CREATE INDEX idx_users_name_phone ON Users (name, phone_number);
CREATE INDEX idx_txn_time         ON Transactions (transaction_time);
CREATE INDEX idx_txn_category     ON Transactions (category_id);
CREATE INDEX idx_txn_sender       ON Transactions (sender_id);
CREATE INDEX idx_txn_recipient    ON Transactions (recipient_id);
CREATE INDEX idx_txn_agent        ON Transactions (agent_id);
CREATE INDEX idx_party_user       ON Transaction_Parties (user_id);
CREATE INDEX idx_logs_process_time ON System_Logs (process_name, logged_at);

-- ---------- SAMPLE INSERTS ----------

INSERT INTO Transaction_Categories (category_name, description)
VALUES
    ('deposit', 'Money received into the account.'),
    ('withdrawal', 'Money withdrawn through an agent or cash-out.'),
    ('transfer', 'Money sent to another mobile money account.'),
    ('payment', 'Payment for goods or services.'),
    ('airtime', 'Purchase of mobile airtime.'),
    ('data_bundle', 'Purchase of a mobile data bundle.'),
    ('other', 'Transaction that does not match a known category.');

INSERT INTO Users (name, phone_number, account_number, type)
VALUES
    ('Abebe Chala CHEBUDIE', NULL, '36521838', 'self'),
    ('Agent Sophia',         '250790777777', NULL, 'agent'),
    ('Jean Uwase',           '250788123456', '45001234', 'individual'),
    ('Kigali Market Ltd',    '250788654321', '51007890', 'individual'),
    ('Employer Payroll',     NULL, '99001122', 'deposit_source');

INSERT INTO Transactions
    (amount, transaction_time, fee, new_balance, tx_id, financial_transaction_id, external_transaction_id, status, category_id, sender_id, recipient_id, agent_id)
VALUES
    (20000.00, '2024-05-26 09:15:00', 500.00, 80000.00, 'TXN-0001', 'FIN-0001', NULL, 'completed', 2, 1, NULL, 2),
    (50000.00, '2024-05-27 08:00:00', 0.00, 130000.00, 'TXN-0002', 'FIN-0002', NULL, 'completed', 1, 5, 1, NULL),
    (15000.00, '2024-05-28 13:40:00', 0.00, 115000.00, 'TXN-0003', 'FIN-0003', 'EXT-0003', 'completed', 3, 1, 3, NULL),
    (8500.00, '2024-05-29 18:20:00', 0.00, 106500.00, 'TXN-0004', 'FIN-0004', 'EXT-0004', 'completed', 4, 1, 4, NULL),
    (2500.00, '2024-05-30 07:05:00', 0.00, 104000.00, 'TXN-0005', 'FIN-0005', NULL, 'completed', 5, 1, NULL, NULL);

INSERT INTO Transaction_Parties (transaction_id, user_id, party_role)
VALUES
    (1, 1, 'sender'), (1, 2, 'agent'),
    (2, 5, 'sender'), (2, 1, 'recipient'),
    (3, 1, 'sender'), (3, 3, 'recipient'),
    (4, 1, 'sender'), (4, 4, 'recipient'),
    (5, 1, 'sender');

INSERT INTO System_Logs (process_name, log_level, message, records_affected)
VALUES
    ('xml_parser', 'INFO', 'XML file parsed successfully.', 5),
    ('clean_normalize', 'INFO', 'Amounts and phone numbers normalized.', 5),
    ('categorize', 'INFO', 'Transactions assigned to categories.', 5),
    ('load_database', 'INFO', 'Transactions loaded into database.', 5),
    ('load_database', 'WARNING', 'One transaction did not include an external reference.', 1);

-- ---------- CRUD TEST QUERIES ----------
-- SELECT: list transactions with their category and recipient.
SELECT t.transaction_id, t.amount, c.category_name, recipient.name AS recipient_name
FROM Transactions AS t
JOIN Transaction_Categories AS c ON c.category_id = t.category_id
LEFT JOIN Users AS recipient ON recipient.user_id = t.recipient_id;

-- UPDATE: correct a transaction status, then verify it.
UPDATE Transactions SET status = 'reversed' WHERE tx_id = 'TXN-0005';
SELECT tx_id, status FROM Transactions WHERE tx_id = 'TXN-0005';

-- DELETE: remove a test log without affecting transaction records.
DELETE FROM System_Logs WHERE message = 'Temporary CRUD test log.';