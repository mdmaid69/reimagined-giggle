  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))