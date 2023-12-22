import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import collections
def create_priority_queue():
        return collections.deque()