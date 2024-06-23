#arithmetic operators
print(2**3)
print(2+3)
print(2-5)
print(2*3)
print(2/3)
print(2//3)#floor division
print(2.0//5) # floor div rounds the value
print(5%2)

result=0
#result=result+10
result+=10 #same

#to stop float conversion in division
print(int(4 / 2))
print(round(4 / 3, 2))
print(round(2.4444, 2)) # 2 decimal after .

#binary operator
print(2-2)
#unary operatoes
print(-6-6)

#comparison operators  gives True/False - boolean
print(2==2) #equal to
print(3!=4) #not equal to 
print(5>=3) #greater than or equal to 
print(5<=3 )#lesser than or equal to
print(5>3)  #strictly greater
print(5<3)  #strictly lesser

#logical operators
a=3
b=4

print(a>10 and b<5) # and operator - returns true if both are true
print(a>5 or b<6)   # or operator - returns true if any one is true
print(not(a==5))    #not is opposite to the statement result

#bitwise operators
# AND: Performs bitwise AND operation on each pair of corresponding bits
result_and = 5 & 3  # 5 (0b0101) & 3 (0b0011) = 1 (0b0001)

# OR: Performs bitwise OR operation on each pair of corresponding bits
result_or = 5 | 3  # 5 (0b0101) | 3 (0b0011) = 7 (0b0111)

# XOR: Performs bitwise XOR operation on each pair of corresponding bits
result_xor = 5 ^ 3  # 5 (0b0101) ^ 3 (0b0011) = 6 (0b0110)

# NOT: Inverts each bit (1's complement)
result_not = ~5  # ~5 (0b0101) = -6 (two's complement of 0b1010)

# LEFT SHIFT: Shifts bits to the left, filling with 0s from the right (also multiplication of (left_value*(2^value in right))
result_left_shift = 5 << 1  # 5 (0b0101) << 1 = 10 (0b1010)

# RIGHT SHIFT: Shifts bits to the right, filling with sign bit (leftmost bit) from the left (fraction of the left)
result_right_shift = 5 >> 1  # 5 (0b0101) >> 1 = 2 (0b0010)
