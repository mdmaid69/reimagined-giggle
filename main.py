sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)