  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())