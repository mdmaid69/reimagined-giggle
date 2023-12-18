sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import os
  def get_base_name(path):
        return os.path.basename(path)