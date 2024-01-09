  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
text = "Hello, world!"
print("Uppercase:", text.upper())