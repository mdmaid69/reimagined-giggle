import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import collections
def create_user_list():
        return collections.UserList()