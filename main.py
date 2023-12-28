import shutil
def delete_directory(path):
        shutil.rmtree(path)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)