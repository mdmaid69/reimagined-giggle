def calculate_average(numbers):
        return sum(numbers) / len(numbers)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b