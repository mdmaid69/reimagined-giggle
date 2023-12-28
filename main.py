import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)