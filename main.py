import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"