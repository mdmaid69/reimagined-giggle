n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"