n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))