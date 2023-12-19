import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)