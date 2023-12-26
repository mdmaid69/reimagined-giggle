  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)