import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)