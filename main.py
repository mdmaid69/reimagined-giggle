sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)