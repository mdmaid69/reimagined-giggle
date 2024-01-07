  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def count_words(sentence):
        return len(sentence.split())