  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities