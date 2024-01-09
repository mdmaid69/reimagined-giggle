  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
n = 10
print("Powers of 2:", [2**x for x in range(n)])