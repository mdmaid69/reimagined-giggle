sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)