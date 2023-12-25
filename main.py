  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def find_difference(list1, list2):
        return set(list1) - set(list2)