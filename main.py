import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))