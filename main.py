import json
print(json.dumps({"name": "John", "age": 30}))
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities