import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()