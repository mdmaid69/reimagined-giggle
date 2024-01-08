def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)