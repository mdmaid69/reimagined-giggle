def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b