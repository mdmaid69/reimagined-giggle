  import os
  def get_base_name(path):
        return os.path.basename(path)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())