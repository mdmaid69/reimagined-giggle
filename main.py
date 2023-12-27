def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)