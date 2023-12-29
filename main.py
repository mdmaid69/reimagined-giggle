import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())