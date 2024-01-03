def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import json
print(json.dumps({"name": "John", "age": 30}))