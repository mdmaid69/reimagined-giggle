import json
def convert_to_json(data):
        return json.dumps(data)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])