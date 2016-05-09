#user key split into L array
l = [0X13733624,0X13733624,0X13733624,0X13733624] 

# initial values of S array
S = [0xb7e15163,0x5618cb1c,0Xf45044d5,0x9287be8e,0x30bf3847,0xcef6b200,0x6d2e2bb9,0x0b65a572,0xa99d1f2b,0x47d498e4,0xe60c129d,0x84438c56,
       0x227b060f,0xc0b27fc8,0x5ee9f981,0xfd21733a,0x9b58ecf3,0x399066ac,0xd7c7e065,0x75ff5a1e,0x1436d3d7,0xb26e4d90,0x50a5c749,0xeedd4102,0x8d14babb,0x2b4c3474] 

# left rotate function
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# initializing all the variables    
a_reg = 0
b_reg = 0
i_cnt = 0 
j_cnt = 0
k_cnt = 0
max_bits = 32

# do 78 times    
for k_cnt in range(0,78):
        
    #A = S[i] = (S[i] + A + B) <<< 3;

    a = S[i_cnt] + a_reg + b_reg # S[i] + A + B
    a_circ = rol(a, 3, max_bits) # <<< 3
    a_reg = a_circ               # A = S[i] + A + B
    S[i_cnt] = a_circ            # S[i] = S[i] + A + B

    #B = L[j] = (L[j] + A + B) <<< (A + B);
    temp = a_circ + b_reg        # A + B
    b = temp + l[j_cnt]          # L[j] + A + B
    b_circ = rol(b, temp & 0x1F, max_bits) # <<< A + B
    b_reg = b_circ               # B = L[j] + A + B
    l[j_cnt] = b_circ            # L[j] = L[j] + A + B
    
    # i = (i + 1) mod 26 
    if(i_cnt >= 25 ):
        i_cnt = 0
    else: i_cnt = i_cnt + 1
    
    #j = (j + 1) mod 4;
    if(j_cnt >= 3 ):
        j_cnt = 0
    else: j_cnt = j_cnt + 1
                              
print "S values are : "         # printing S values values
for i_cnt in range(0,26):
    print hex(S[i_cnt])