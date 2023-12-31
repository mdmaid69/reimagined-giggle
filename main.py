  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())