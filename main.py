import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)