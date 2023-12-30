import platform
def get_os_info():
        return platform.uname()
text = "Hello, world!"
print("Words:", len(text.split()))