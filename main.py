import tensorflow as tf
print(tf.__version__)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)