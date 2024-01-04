  def convert_to_hex(n):
        return hex(n)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)