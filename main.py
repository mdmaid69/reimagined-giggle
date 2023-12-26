  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
n = 10
print("Cube numbers:", [x**3 for x in range(n)])