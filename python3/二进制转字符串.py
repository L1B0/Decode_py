def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
def __main__():
         a = input("")
         b = input("")
         if a == 'e':
                  print(encode(b))
         else:
                  print(decode(b))
__main__()
