sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"