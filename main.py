text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"