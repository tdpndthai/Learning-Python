# Variable x holds 10 and variable y holds 5
x = 5
y = 10
x += y
print ("Value of a post x+=y is ", x)
x *= y
print ("Value of a post x*=y is ", x)
x /= y
print ("Value of a post x/=y is ", x)
x %= y
print ("Value of a post x%=y is ", x)
x **= y
print ("Value of x post x**=y is ", x)
x //= y
print ("Value of a post x//=y is ", x)


# -------- output --------
# Value of a post x+=y is 15
# Value of a post x*=y is 150
# Value of a post x/=y is 15.0
# Value of a post x%=y is 5.0
# Value of x post x**=y is 9765625.0
# Value of a post x//=y is 976562.0