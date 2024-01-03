n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  def calculate_area_triangle(b, h):
        return 0.5 * b * h