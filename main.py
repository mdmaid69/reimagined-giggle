  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))