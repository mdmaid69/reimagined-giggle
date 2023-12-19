def is_palindrome(s):
        return s == s[::-1]
import json
def convert_to_json(data):
        return json.dumps(data)