import hashlib

for i in range(32,127):
           for j in range(32,127):
                     for k in range(32,127):
                              flag = 'TASC'+chr(i)+'O3RJMV'+chr(j)+'WDJKX'+chr(k)+'ZM'
                              m1 = hashlib.md5()
                              m1.update(flag)
                              if (m1.hexdigest())[:5] == 'e9032':
                                       print(flag, m1.hexdigest())
