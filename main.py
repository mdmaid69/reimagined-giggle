import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list