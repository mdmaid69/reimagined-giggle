  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b