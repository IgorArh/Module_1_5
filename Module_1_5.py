immutable_var = (10, "five", 3.0 , [1,2,3] , True)
print(immutable_var)


#immutable_var[0]= 5
#TypeError: 'tuple' object does not support item assignment
#Главное свойство кортежа - это невозможность изменить содержимое


mutable_list = [10 , 'five' , True , [1,2,3]]
mutable_list[0] = 12
mutable_list[2] = False
mutable_list.extend(['apple', 3.0])
print(mutable_list)