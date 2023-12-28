  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))