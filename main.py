def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def delete_file(file_name):
        os.remove(file_name)