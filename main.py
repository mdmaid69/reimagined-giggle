numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True