import base64
a = input("input your strings:")
flag = ''
for i in range(-64,64):
         flag = ''
         for j in range(len(a)):
                  flag += chr(ord(a[j])-i)
         print(flag)
