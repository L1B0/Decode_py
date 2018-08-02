import base64
a = input("input your strings:")
flag = ''
for i in range(1,26):
         flag = ''
         for j in range(len(a)):
                  if a[j] <= 'z' and a[j] >= 'a':
                           flag += chr( (ord(a[j])-ord('a')+i)%26 + ord('a') )
                  elif a[j] <= 'Z' and a[j] >= 'A':
                           flag += chr( (ord(a[j])-ord('A')+i)%26 + ord('A') )
                  elif a[j] >= '0' and a[j] <= '9':
                           flag += a[j]
                  else:
                           flag += a[j]
         flag = base64.b64decode(flag.encode(encoding="utf-8"))
         print(flag)
