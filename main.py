  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time