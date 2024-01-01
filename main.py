  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))