  import sys
  def get_python_version():
        return sys.version
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])