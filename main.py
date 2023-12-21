  import os
  def get_current_directory():
        return os.getcwd()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))