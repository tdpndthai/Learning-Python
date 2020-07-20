none = None #singleton null object
boolean = bool(True)
integer = 1
Long = 3.14
# float
Float = 3.14
Float_inf = float('inf')
Float_nan = float('nan')
# complex object type, note the usage of letter j
Complex = 2+8j
# string can be enclosed in single or double quote
string = 'this is a string'
me_also_string = "also me"
List = [1, True, 'ML'] # Values can be changed
Tuple = (1, True, 'ML') # Values can not be changed
Set = set([1,2,2,2,3,4,5,5]) # Duplicates will not be stored
# Use a dictionary when you have a set of unique keys that map to values
Dictionary = {'a':'A', 2:'AA', True:1, False:0}
# lets print the object type and the value
print (type(none), none)
print (type(boolean), boolean)
print (type(integer), integer)
print (type(Long), Long)
print (type(Float), Float)
print (type(Float_inf), Float_inf)
print (type(Float_nan), Float_nan)
print (type(Complex), Complex)
print (type(string), string)
print (type(me_also_string), me_also_string)
print (type(Tuple), Tuple)
print (type(List), List)
print (type(Set), Set)
print (type(Dictionary), Dictionary)