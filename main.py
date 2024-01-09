  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())