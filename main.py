  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
from collections import Counter
print(Counter("hello world"))