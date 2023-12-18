def is_palindrome(s):
        return s == s[::-1]
import json
def read_from_json(json_string):
        return json.loads(json_string)