import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()