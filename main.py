  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())