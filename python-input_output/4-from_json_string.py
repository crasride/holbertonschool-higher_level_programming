#!/usr/bin/python3
"""
returns an object (Python data structure)
represented by a JSON string
method - loads() del modulo json de python
"""
import json


def from_json_string(my_str):
    """ Convert JSON object a Python object """
    return json.loads(my_str)
