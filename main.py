  def is_odd(n):
        return n % 2 != 0
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)