  def remove_duplicates(lst):
        return list(set(lst))
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b