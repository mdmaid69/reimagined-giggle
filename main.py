def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))