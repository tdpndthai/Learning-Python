# Basic six bitwise operations
# Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
x = 10
y = 4
print (x >> y) # Right Shift
print (x << y) # Left Shift
print (x & y) # Bitwise AND
print (x | y) # Bitwise OR
print (x ^ y) # Bitwise XOR
print (~x) # Bitwise NOT


# -------- output --------
# 0
# 160
# 0
# 14
# 14
# -11