  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))