immutable_var = 1, 2, 'apple', 5.5
print(immutable_var)
#immutable_var[3] = 9 # выдает ошибку(не изменяемая переменная)
print(immutable_var)
print(type(immutable_var))

mutable_list = [1, 2, 'banana', 7.8]
print(mutable_list)
mutable_list[1] = 'apple'
print(mutable_list)
print(type(mutable_list))