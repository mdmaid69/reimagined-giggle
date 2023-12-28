import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)