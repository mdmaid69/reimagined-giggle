def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev