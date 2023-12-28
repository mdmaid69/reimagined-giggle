import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)