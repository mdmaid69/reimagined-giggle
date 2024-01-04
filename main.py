import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello, World!"