  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))