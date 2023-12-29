numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)