  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])