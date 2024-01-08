  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))