  import os
  def get_directory_name(path):
        return os.path.dirname(path)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))