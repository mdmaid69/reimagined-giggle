import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue