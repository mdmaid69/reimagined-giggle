import glob
def find_files(pattern):
        return glob.glob(pattern)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)