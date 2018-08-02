import base64
from Crypto.Cipher import AES
password = base64.b64decode("cGhyYWNrICBjdGYgMjAxNg==")
content = base64.b64decode("sSNnx1UKbYrA1+MOrdtDTA==")

handle = AES.new( password , AES.MODE_CBC , '\x00'*16 )

print( handle.decrypt( content ) )

'''https://www.jarvisoj.com/challenges Smali'''
