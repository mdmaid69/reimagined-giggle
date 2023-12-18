  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())