sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)