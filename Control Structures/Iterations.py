#câu lệnh điều khiển vòng lặp for và while

# First Example
print ("First Example")
for item in [1,2,3,4,5]:
    print ('item :', item)
# Second Example
print ("Second Example")
letters = ['A', 'B', 'C']
for letter in letters:
    print ('First loop letter :', letter)

# Third Example - Iterating by sequency index
print ("Third Example")
for index in range(len(letters)):
    print ('First loop letter :', letters[index])
# Fourth Example - Using else statement
print ("Fourth Example")
for item in [1,2,3,4,5]:
    print ('item :', item)
else:
    print ('looping over item complete!')
# ----- output ------
# First Example
# item : 1
# item : 2
# item : 3
# item : 4
# item : 5
# Second Example
# First loop letter : A
# First loop letter : B
# First loop letter : C
# Third Example
# First loop letter : A
# First loop letter : B
# First loop letter : C
# Fourth Example
# item : 1
# item : 2
# item : 3
# item : 4
# item : 5
# looping over item complete!

#Example Code for a “while” Loop Statement
count = 0
while (count < 5):
    print ('The count is:', count)
count = count + 1

# ----- output ------
# The count is: 0
# The count is: 1
# The count is: 2
# The count is: 3
# The count is: 4

#Example Code for a “while” with an “else” Statement

count = 0
while count < 5:
    print (count, " is less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")

# ----- output ------
# 0 is less than 5
# 1 is less than 5
# 2 is less than 5
# 3 is less than 5
# 4 is less than 5
# 5 is not less than 5