  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps