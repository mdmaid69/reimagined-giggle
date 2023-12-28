def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)