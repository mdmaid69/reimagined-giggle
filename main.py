import os
def get_environment_variable(var):
        return os.getenv(var)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)