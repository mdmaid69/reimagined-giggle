  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)