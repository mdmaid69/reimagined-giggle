import platform
def get_os_info():
        return platform.uname()
import re
print(re.match("h.*o", "hello world"))