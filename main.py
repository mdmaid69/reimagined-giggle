  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))