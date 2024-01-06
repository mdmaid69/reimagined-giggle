  def convert_to_binary(n):
        return bin(n)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)