  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)