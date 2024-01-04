  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())