text = "Hello, world!"
print("Uppercase:", text.upper())
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)