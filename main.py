sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)