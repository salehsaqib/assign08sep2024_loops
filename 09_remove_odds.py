# 9. *Write a program* to remove all the odd numbers from an array.

my_list = [2,5,7,8,11,17,20,21,22,8]
print(my_list)
i = 0
new_list = []
while i < len(my_list):
    list_item:int = int(my_list[i])
    if list_item%2==0:
        new_list.append(list_item)    
    i = i + 1
print(new_list)
