def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import json
def read_from_json(json_string):
        return json.loads(json_string)