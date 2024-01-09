  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def count_words(sentence):
        return len(sentence.split())