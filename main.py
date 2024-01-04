import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)