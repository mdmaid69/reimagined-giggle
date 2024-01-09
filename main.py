sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)