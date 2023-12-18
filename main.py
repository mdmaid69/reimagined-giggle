  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())