  def is_odd(n):
        return n % 2 != 0
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b