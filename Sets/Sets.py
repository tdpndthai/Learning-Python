#không có thứ tự ,ko có mục trùng lặp được lưu trữ,các mục trong 1 bộ có thể thay đổi

# Creating an empty set
languages = set( )
print (type(languages), languages)
languages = {'Python', 'R', 'SAS', 'Julia'}
print (type(languages), languages)
# set of mixed datatypes
mixed_set = {"Python", (2.7, 3.4)}
print (type(mixed_set), languages)