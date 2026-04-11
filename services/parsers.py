import re


def extract_eth_amount(text):
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*ETH", text, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None