import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import tensorflow as tf
print(tf.__version__)