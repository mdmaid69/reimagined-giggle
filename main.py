  import os
  def get_base_name(path):
        return os.path.basename(path)
def find_unique_words(sentence):
        return set(sentence.split())