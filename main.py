  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))