  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])