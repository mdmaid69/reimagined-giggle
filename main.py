  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())