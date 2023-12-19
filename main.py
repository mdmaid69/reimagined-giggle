n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True