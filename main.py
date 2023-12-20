def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)