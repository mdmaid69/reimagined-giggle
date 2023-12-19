def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)