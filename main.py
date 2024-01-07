import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def convert_to_octal(n):
        return oct(n)