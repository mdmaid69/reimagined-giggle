import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)