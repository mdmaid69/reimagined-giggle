  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
def find_unique_words(sentence):
        return set(sentence.split())