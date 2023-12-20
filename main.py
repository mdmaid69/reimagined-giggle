  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def find_unique_words(sentence):
        return set(sentence.split())