import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets