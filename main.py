import json
print(json.dumps({"name": "John", "age": 30}))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time