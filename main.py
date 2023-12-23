  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))