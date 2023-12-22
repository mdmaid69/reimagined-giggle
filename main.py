  import os
  def delete_file(file_name):
        os.remove(file_name)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))