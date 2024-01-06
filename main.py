def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)