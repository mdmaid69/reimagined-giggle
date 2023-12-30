import shutil
def delete_directory(path):
        shutil.rmtree(path)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()