import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import math
def calculate_permutations(n, k):
        return math.perm(n, k)