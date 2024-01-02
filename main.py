  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))