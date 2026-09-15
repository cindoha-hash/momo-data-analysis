-- Reject a transaction that would leave a negative balance.
DELIMITER //
CREATE TRIGGER prevent_negative_balance
BEFORE INSERT ON Transactions
FOR EACH ROW
BEGIN
    IF NEW.new_balance IS NOT NULL AND NEW.new_balance < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Transaction would result in negative balance';
    END IF;
END//
DELIMITER ;

-- Prevent a user from being both sender and recipient.
ALTER TABLE Transactions
ADD CONSTRAINT chk_sender_recipient_different
CHECK (sender_id IS NULL OR recipient_id IS NULL OR sender_id != recipient_id);