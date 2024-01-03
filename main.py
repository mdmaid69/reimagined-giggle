def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)