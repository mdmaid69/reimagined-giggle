def calculate_average(lst):
        return sum(lst) / len(lst)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b