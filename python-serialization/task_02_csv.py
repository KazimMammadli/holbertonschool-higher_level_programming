#!/usr/bin/python3
"""
reading data from one format (CSV) and converting
 it into another format (JSON) using serialization techniques.
"""
import json
import csv


def convert_csv_to_json(csv_file):
    """Read the csv file and write to the json file."""
    try:
        with open(csv_file, 'r') as csv_file:
            with open("data.json", 'w') as json_file:  
                json.dump(csv.DictReader, json_file)
        return True
    except Exception:
        return False
