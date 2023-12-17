  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)