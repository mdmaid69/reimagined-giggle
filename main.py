  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))