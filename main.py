sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)