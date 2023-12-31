sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)