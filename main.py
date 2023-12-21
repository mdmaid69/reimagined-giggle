n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)