  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())