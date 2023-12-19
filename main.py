  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))