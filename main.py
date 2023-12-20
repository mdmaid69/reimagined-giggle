import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])