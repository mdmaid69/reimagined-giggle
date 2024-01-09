  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())