  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())