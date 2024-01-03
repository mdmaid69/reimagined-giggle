  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def find_unique_words(sentence):
        return set(sentence.split())