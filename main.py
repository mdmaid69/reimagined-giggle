def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)