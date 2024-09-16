# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.

my_list = [-45,-5,-12,-78,79,102,111,-89,-3,-9,-7]
print(my_list)
i = 0
new_list = []
while i < len(my_list):
    list_item:int = int(my_list[i])
    if list_item > 0:
        new_list.append(list_item)    
    i = i + 1
print(new_list)
