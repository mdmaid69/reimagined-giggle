  import sys
  def get_python_version():
        return sys.version
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)