def count_words(sentence):
        return len(sentence.split())
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)