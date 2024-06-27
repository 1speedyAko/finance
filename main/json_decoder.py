import json

with open('datadump_utf8_bom_removed.json', 'r', encoding='utf-8') as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
