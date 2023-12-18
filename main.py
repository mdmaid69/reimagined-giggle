def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)