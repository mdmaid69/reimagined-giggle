import json
print(json.dumps({"name": "John", "age": 30}))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)