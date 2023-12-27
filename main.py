import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding