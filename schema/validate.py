# /// script
# dependencies = [
#   "jsonschema==4.22.0",
# ]
# ///

import json
import sys
from jsonschema import validate, ValidationError

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    return schema

def validate_file(schema_path, file_path):
    schema = load_schema(schema_path)

    with open(file_path, 'r') as f:
        data = json.load(f)

    try:
        validate(instance=data, schema=schema)
        print(f"{file_path} has valid schema.")
    except ValidationError as e:
        print(f"{file_path} has invalid schema: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_file('./schema/assetlist.json', './assetlist.json')