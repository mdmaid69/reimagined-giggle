text = "Hello, world!"
print("Characters:", len(text))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)