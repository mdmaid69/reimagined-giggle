  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])