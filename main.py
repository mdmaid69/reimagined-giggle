  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))