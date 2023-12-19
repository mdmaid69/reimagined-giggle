  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def find_unique_words(sentence):
        return set(sentence.split())