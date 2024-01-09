def count_words(sentence):
        return len(sentence.split())
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode