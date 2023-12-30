def count_words(sentence):
        return len(sentence.split())
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)