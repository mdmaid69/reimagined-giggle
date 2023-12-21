import platform
def get_os_info():
        return platform.uname()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)