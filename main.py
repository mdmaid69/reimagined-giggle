  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())