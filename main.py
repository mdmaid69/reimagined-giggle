import json
print(json.dumps({"name": "John", "age": 30}))
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal