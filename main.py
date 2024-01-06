import json
def read_from_json(json_string):
        return json.loads(json_string)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding