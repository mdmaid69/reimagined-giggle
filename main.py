n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)