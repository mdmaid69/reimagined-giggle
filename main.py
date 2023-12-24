import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)