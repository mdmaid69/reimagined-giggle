def is_palindrome(s):
        return s == s[::-1]
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)