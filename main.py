  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())