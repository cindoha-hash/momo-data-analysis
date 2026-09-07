import unittest
from etl.parse_xml import parse_xml


class TestParseXML(unittest.TestCase):
    def test_returns_list(self):
        # TODO: point to a small sample XML file for testing
        result = []
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
