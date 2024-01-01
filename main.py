  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))