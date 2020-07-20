# Các câu lệnh lựa chọn cho phép các lập trình viên kiểm tra một điều kiện và, dựa trên kết quả,
# thực hiện các hành động khác nhau. Có hai phiên bản của cấu trúc hữu ích này: 1) if và 2) if -else,

#Example Code for a Simple “if” Statement
var = -1
if var < 0:
    print(var) #in ra giá trị biến
    print("the value of var is negative")
# If the suite of an if clause consists only of a single line, it may go on
#the same line as the header statement
if (var == -1):
    print("the value of var is negative")


# -------- output --------
# -1
# the value of var is negative
# the value of var is negative

#Example Code for “if else” Statement

var = 1
if var < 0:
    print ("the value of var is negative")
    print (var)
else:
    print ("the value of var is positive")
    print (var)
# -------- output --------
# the value of var is positive
# 1

#Example Code for Nested “if else” Statements
score = 95
if score >= 99:
    print('A')
elif score >=75:
    print('B')
elif score >= 60:
    print('C')
elif score >= 35:
    print('D')
else:
    print('F')
    
# -------- output --------
# B