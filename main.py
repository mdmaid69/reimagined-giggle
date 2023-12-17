def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)