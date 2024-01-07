n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)