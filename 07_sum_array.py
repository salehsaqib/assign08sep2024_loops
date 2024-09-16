# 7. *Create a function* that takes an array of numbers as a parameter. 
# Use a while loop to calculate and return the sum of all the numbers in the array.
def array_sum(my_list:list):
    i = 0    
    sum = 0
    while i < len(my_list):
        list_item:int = int(my_list[i])
        sum = sum + list_item
        i = i + 1
    print(sum)

my_list = [1,2,3,4,5]
array_sum(my_list)


