  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def find_unique_words(sentence):
        return set(sentence.split())