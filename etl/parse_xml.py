"""
Parses raw MoMo SMS XML into a list of transaction dicts.
Implementation to be completed in Phase 2 (Data Processing).
"""
import xml.etree.ElementTree as ET
from etl.config import XML_INPUT_PATH


def parse_xml(file_path: str = XML_INPUT_PATH):
    """
    Parse the MoMo XML file and return a list of raw transaction records.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    transactions = []
    # TODO: loop through XML nodes and extract transaction fields
    # for sms in root.findall("sms"):
    #     transactions.append({...})

    return transactions


if __name__ == "__main__":
    data = parse_xml()
    print(f"Parsed {len(data)} transactions")
