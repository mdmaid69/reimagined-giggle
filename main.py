  def calculate_area_circle(r):
        return 3.14 * r**2
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))