sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]