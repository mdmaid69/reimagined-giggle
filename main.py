import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])