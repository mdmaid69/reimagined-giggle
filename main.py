def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)