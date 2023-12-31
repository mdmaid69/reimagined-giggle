  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))