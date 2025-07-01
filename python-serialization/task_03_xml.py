#!/usr/bin/python3
"""Serialization and deserialization using XML
as an alternative format to JSON."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
