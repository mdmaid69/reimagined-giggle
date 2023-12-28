import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)