import collections
def create_queue():
        return collections.deque()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)