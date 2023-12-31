import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"