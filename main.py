  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_perpetuity(payment, rate):
        return payment / rate