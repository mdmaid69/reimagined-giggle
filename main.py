import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def is_palindrome(s):
        return s == s[::-1]