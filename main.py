  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
def count_words(sentence):
        return len(sentence.split())