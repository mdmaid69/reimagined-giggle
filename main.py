import json
print(json.dumps({"name": "John", "age": 30}))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())