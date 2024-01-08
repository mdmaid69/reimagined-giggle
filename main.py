sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)