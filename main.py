  def convert_to_hex(n):
        return hex(n)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b