  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b