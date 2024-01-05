  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)