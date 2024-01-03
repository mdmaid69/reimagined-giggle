def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def get_current_directory():
        return os.getcwd()