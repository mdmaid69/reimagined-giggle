sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)