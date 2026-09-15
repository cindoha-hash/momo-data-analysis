-- ---------- USERS ----------
CREATE TABLE Users (
    user_id         INTEGER         PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(100)    NOT NULL,
    phone_number    VARCHAR(20)     NULL,
    account_number  VARCHAR(30)     NULL,
    type            ENUM('self','individual','deposit_source','agent') NOT NULL
) COMMENT = 'People and entities that appear as a party to a transaction: the account holder, named recipients, deposit sources, and agents.';


-- ---------- TRANSACTION_CATEGORIES ----------
CREATE TABLE Transaction_Categories (
    category_id     INTEGER         PRIMARY KEY AUTO_INCREMENT,
    category_name   ENUM('payment','transfer','deposit','withdrawal','airtime','data_bundle') NOT NULL
) COMMENT = 'Lookup table for what kind of transaction an event is. One category, many transactions.';


-- ---------- TRANSACTIONS ----------
CREATE TABLE Transactions (
    transaction_id           INTEGER         PRIMARY KEY AUTO_INCREMENT,
    amount                   DECIMAL(15,2)   NOT NULL,
    transaction_time         DATETIME        NOT NULL,
    fee                      DECIMAL(15,2)   NULL,
    new_balance              DECIMAL(15,2)   NULL,
    tx_id                    VARCHAR(50)     NULL,
    financial_transaction_id VARCHAR(50)     NULL,
    external_transaction_id  VARCHAR(50)     NULL,
    status                   ENUM('completed','failed','reversed') NOT NULL,
    category_id              INTEGER         NOT NULL,
    sender_id                INTEGER         NULL,
    recipient_id             INTEGER         NULL,
    agent_id                 INTEGER         NULL,
    FOREIGN KEY (category_id)   REFERENCES Transaction_Categories(category_id),
    FOREIGN KEY (sender_id)     REFERENCES Users(user_id),
    FOREIGN KEY (recipient_id)  REFERENCES Users(user_id),
    FOREIGN KEY (agent_id)      REFERENCES Users(user_id),
    CHECK (amount >= 0),
    CHECK (fee IS NULL OR fee >= 0),
    CHECK (new_balance IS NULL OR new_balance >= 0)
) COMMENT = 'One row per transaction event. Holds everything specific to a single event; parties are referenced by FK to Users.';


CREATE INDEX idx_users_name_phone ON Users (name, phone_number);
CREATE INDEX idx_txn_time         ON Transactions (transaction_time);
CREATE INDEX idx_txn_category     ON Transactions (category_id);
CREATE INDEX idx_txn_sender       ON Transactions (sender_id);
CREATE INDEX idx_txn_recipient    ON Transactions (recipient_id);
CREATE INDEX idx_txn_agent        ON Transactions (agent_id);

-- ---------- SAMPLE INSERTS ----------

INSERT INTO Transaction_Categories (category_name)
VALUES ('withdrawal');

INSERT INTO Users (name, phone_number, account_number, type)
VALUES
    ('Abebe Chala CHEBUDIE', NULL, '36521838', 'self'),
    ('Agent Sophia',         '250790777777', NULL, 'agent');

INSERT INTO Transactions
    (amount, transaction_time, fee, new_balance, tx_id, status, category_id, sender_id, agent_id)
VALUES
    (20000.00, '2024-05-26 00:00:00', NULL, NULL, NULL, 'completed', 1, 1, 2);