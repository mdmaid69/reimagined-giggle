  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)