text = "Hello, world!"
print("Characters:", len(text))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)