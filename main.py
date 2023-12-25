  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)