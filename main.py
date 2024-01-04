  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())