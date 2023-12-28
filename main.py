import json
def convert_to_json(data):
        return json.dumps(data)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])