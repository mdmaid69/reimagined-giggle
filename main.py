def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)