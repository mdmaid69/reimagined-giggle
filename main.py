  import os
  def split_path(path):
        return os.path.split(path)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))