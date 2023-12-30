  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def find_unique_words(sentence):
        return set(sentence.split())