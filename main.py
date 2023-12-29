import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
i = 0
while i < 5:
        print(i)
        i += 1