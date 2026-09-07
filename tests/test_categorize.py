import unittest
from etl.categorize import categorize_transaction


class TestCategorize(unittest.TestCase):
    def test_deposit(self):
        txn = {"message": "You have received a deposit of 1000 RWF"}
        self.assertEqual(categorize_transaction(txn), "deposit")

    def test_unknown(self):
        txn = {"message": "Some random message"}
        self.assertEqual(categorize_transaction(txn), "other")


if __name__ == "__main__":
    unittest.main()
