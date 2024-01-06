import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"