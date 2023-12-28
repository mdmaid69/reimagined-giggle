text = "Hello, world!"
print("Reversed:", text[::-1])
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)