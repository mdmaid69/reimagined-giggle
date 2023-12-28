  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))