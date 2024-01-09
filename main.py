  def is_odd(n):
        return n % 2 != 0
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b