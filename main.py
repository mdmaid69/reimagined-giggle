import sys
def exit_program():
        sys.exit()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)