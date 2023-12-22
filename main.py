  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())