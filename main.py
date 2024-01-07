import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
for i in range(10): print(i)