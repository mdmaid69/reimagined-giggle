import collections
def create_queue():
        return collections.deque()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"