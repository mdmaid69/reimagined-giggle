import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import logging
def log_message(message):
        logging.info(message)