  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
def is_palindrome(s):
        return s == s[::-1]