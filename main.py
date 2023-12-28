  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())