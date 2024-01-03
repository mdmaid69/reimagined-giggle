import collections
def create_stack():
        return collections.deque()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)