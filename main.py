n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c