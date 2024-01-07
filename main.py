text = "Hello, world!"
print("Words:", len(text.split()))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)