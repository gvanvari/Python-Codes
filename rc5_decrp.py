A = 0x0e3eeaf3
B = 0xC60E33DB

print "A = ", format(A, '08x')
print "B = ", format(B, '08x')

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 
max_bits = 32  

s =( 0X9BBBD8C8,0X1A37F7FB,0X46F8E8C5,0X460C6085,0X70F83B8A,0X284B8303,
						0X513E1454,0XF621ED22,0X3125065D,0X11A83A5D,0XD427686B,0X713AD82D,
						0X4B792F99,0X2799A4DD,0XA7901C49,0XDEDE871A,0X36C03196,0XA7EFC249,
						0X61A78BB8,0X3B0A1D2B,0X4DBFCA76,0XAE162167,0X30D76B0A,0X43192304,0XF6CC1431,0X65046380)

for i in range(12,0,-1):
	print "i = %d" %(i)
	
	B= B - s[2*i+1]
	print "B-s[%d] = %08X " % (2*i+1, B)
	
	B= ror(B, A & 0x1F, max_bits)
	print "BrorA rotated by %08x = % 08x " % (A & 0x1F, B)
	
	B= B^A
	print "BxorA = ", format(B,'08x')
	
	A= A- s[2*i]
	print "A-s[%d] = %08x " % (2*i, A)
	
	A= ror(A, B & 0x1F, max_bits)
	print "BrorA rotated by %08x = % 08x " % (B & 0x1F, A)
	
	A= A^B
	print "BxorA = ", format(A,'08x')
	print ""

B = B - s[1]
A = A - s[0]

if B<0:
	B = 0xFFFFFFFF + 1 + B
else:
	B = B

if A<0:
	A = 0xFFFFFFFF + 1 + A
else:
	A = A

print "Final Result = %08x%08X" % (A,B)
	
	