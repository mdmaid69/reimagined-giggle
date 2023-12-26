import sys
def exit_program():
        sys.exit()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)