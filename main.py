import os
def get_environment_variable(var):
        return os.getenv(var)
import collections
def create_priority_queue():
        return collections.deque()