import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()