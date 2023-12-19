  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))