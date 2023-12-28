import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import sys
def exit_program():
        sys.exit()