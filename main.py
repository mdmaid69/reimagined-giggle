import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity