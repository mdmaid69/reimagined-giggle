  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())