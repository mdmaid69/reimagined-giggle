  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)