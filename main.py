numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))