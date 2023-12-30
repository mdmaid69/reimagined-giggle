  def convert_to_octal(n):
        return oct(n)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)