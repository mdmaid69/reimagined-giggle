import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)