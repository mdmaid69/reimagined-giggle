def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode