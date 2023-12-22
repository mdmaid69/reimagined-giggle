  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())