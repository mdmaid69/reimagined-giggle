import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()