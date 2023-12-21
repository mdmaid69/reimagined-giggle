import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)