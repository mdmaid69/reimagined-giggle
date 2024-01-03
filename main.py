  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time