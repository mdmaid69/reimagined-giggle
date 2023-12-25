  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time