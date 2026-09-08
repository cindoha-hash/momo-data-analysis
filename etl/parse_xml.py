"""Read MoMo SMS XML and return transaction records."""
import xml.etree.ElementTree as ET
from etl.config import XML_INPUT_PATH


def parse_xml(file_path: str = XML_INPUT_PATH):
    """Parse the configured XML file and return its transaction records."""
    tree = ET.parse(file_path)
    root = tree.getroot()

    transactions = []
    return transactions


if __name__ == "__main__":
    data = parse_xml()
    print(f"Parsed {len(data)} transactions")
