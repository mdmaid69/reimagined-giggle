import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"