#!/usr/bin/python3
"""CSV to JSON conversion module"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format"""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = list(reader)
            
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)
            
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
