  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())