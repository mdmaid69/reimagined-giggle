sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev