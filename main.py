import sys
def exit_program():
        sys.exit()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"