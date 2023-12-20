import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])