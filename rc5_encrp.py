A = 0x10100546
B = 0x00000001

s =( 0X9BBBD8C8,0X1A37F7FB,0X46F8E8C5,0X460C6085,0X70F83B8A,0X284B8303,
						0X513E1454,0XF621ED22,0X3125065D,0X11A83A5D,0XD427686B,0X713AD82D,
						0X4B792F99,0X2799A4DD,0XA7901C49,0XDEDE871A,0X36C03196,0XA7EFC249,
						0X61A78BB8,0X3B0A1D2B,0X4DBFCA76,0XAE162167,0X30D76B0A,0X43192304,0XF6CC1431,0X65046380)

A = A + s[0]
B = B + s[1]

print "A = ", format(A, '02x')
print "B = ", format(B, '02x')

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 
max_bits = 32 

for i in range(1,13):
	print "i = %d" %(i)
	A= A^B
	print "AxorB = ", format(A,'02x')
	
	A= rol(A, B & 0x1F, max_bits)
	print "AxorB rotated by %02x = % 02x " % (B & 0x1F, A)
	
	A= A+ s[2*i]
	print "A+s[%d] = %02X " % (2*i, A)
	
	B= B^A
	print "BxorA = ", format(B,'02x')
	
	B= rol(B, A & 0x1F, max_bits)
	print "BxorA rotated by %02x = % 02x " % (A & 0x1F, B)
	
	B= B+ s[2*i+1]
	print "B+s[%d] = %02X " % (2*i+1, B)
	print ""
	
print "Final Result = %02x%02X" % (A,B)
	
	