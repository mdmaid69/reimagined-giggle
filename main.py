  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))