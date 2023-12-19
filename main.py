import itertools
print(list(itertools.permutations([1, 2, 3])))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()