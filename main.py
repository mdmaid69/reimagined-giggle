def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))