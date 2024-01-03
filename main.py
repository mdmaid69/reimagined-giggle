  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))