  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def find_unique_words(sentence):
        return set(sentence.split())