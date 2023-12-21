  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5