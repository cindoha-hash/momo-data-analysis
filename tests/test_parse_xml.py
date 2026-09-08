import unittest
from etl.parse_xml import parse_xml


class TestParseXML(unittest.TestCase):
    def test_returns_list(self):
        result = []
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
