  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def find_unique_words(sentence):
        return set(sentence.split())