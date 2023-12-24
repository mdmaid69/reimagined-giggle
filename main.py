sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)