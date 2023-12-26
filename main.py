import glob
def find_files(pattern):
        return glob.glob(pattern)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)