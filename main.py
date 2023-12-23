  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())