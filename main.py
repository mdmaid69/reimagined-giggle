numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"