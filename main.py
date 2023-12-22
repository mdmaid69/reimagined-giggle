import collections
def create_user_list():
        return collections.UserList()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))