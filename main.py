  def convert_to_binary(n):
        return bin(n)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)