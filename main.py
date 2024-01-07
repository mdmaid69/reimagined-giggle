import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)