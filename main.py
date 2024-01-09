  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def find_unique_words(sentence):
        return set(sentence.split())