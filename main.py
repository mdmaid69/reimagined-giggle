text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)