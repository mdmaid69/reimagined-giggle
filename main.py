import collections
def create_queue():
        return collections.deque()
import os
def get_environment_variable(var):
        return os.getenv(var)