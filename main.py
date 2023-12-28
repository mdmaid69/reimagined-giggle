sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)