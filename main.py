  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])