  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))