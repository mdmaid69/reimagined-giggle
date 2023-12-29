def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]