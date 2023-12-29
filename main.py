  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())