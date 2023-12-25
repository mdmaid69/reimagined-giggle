  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))