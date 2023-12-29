import json
def convert_to_json(data):
        return json.dumps(data)
def count_words(sentence):
        return len(sentence.split())