# Implement a program* that takes a list of temperatures in Celsius as input from the user. 
# Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. 
# Use a while loop to perform the conversion for each temperature.

def insert_list(ulist:list,uindex:int,uval:str)->list:
    ulist.insert(uindex,uval)
    return ulist
    
ent_list:str = str(input("Enter list: e.g ['banana','apple','orange'] : "))
ent_index:int = int(input("Enter Index where to insert value : "))
ent_val:str = str(input("Enter value to insert : "))
ent_list = eval(ent_list)

oldlist = ent_list.copy()
new_list:list = insert_list(ent_list,ent_index,ent_val)
print(f"Old list was : {oldlist}")
print(f"Newly created List is : {new_list}")

# same out put as above code when replace above 4 lines with these below 3 lines
# print(f"Old list was : {ent_list}")
# new_list:list = insert_list(ent_list,ent_index,ent_val)
# print(f"Newly created List is : {new_list}")






