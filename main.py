def calculate_circumference_circle(r):
        return 2 * 3.14 * r
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])