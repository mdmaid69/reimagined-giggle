  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def find_unique_words(sentence):
        return set(sentence.split())