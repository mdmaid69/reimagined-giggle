text = "Hello, world!"
print("Words:", len(text.split()))
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)