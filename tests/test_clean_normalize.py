import unittest
from etl.clean_normalize import normalize_amount, normalize_phone


class TestCleanNormalize(unittest.TestCase):
    def test_normalize_amount(self):
        self.assertEqual(normalize_amount("1,000"), 1000.0)

    def test_normalize_phone(self):
        self.assertEqual(normalize_phone(" 0788123456 "), "0788123456")


if __name__ == "__main__":
    unittest.main()
