def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])