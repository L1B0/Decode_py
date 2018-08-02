from libnum import n2s
import sys   

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

n = 322831561921859
p = 23781539
q = 13574881
e = 23
c = 0xdc2eeeb2782c

d = modinv( e, (q-1)*(p-1) )
print(d)

m = pow( c, d, n )
print( n2s(m) )
