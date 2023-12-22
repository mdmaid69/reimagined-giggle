  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))