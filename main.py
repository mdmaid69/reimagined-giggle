def reverse_string(s):
        return s[::-1]
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b