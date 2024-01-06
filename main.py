def find_unique_words(sentence):
        return set(sentence.split())
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]