sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"