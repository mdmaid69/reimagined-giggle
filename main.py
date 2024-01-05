import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
text = "Hello, world!"
print("Words:", len(text.split()))