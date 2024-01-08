def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5