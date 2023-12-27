  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def count_characters(sentence):
        return len(sentence)