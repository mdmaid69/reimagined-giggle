  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))