  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue