sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns