sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]