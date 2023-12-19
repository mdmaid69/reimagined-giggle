def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def split_path(path):
        return os.path.split(path)