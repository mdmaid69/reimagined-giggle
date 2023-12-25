  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)