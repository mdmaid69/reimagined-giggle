n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
def convert_to_octal(n):
        return oct(n)