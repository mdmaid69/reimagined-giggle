def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import json
def convert_to_json(data):
        return json.dumps(data)