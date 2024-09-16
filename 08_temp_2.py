# Implement a program* that takes a list of temperatures in Celsius as input from the user. 
# Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. 
# Use a while loop to perform the conversion for each temperature.

def conv_temp(cen_temp:int)->int:
    F:float = float(cen_temp * (9/5) + 32)    
    return int(round(F,0))

list_item:str = str(input("Enter list of temperatures in Celsius: e.g [12,45,78] : "))
my_list = eval(list_item)

centi:list = []
i = 0
while i < len(my_list):
    list_item:int = int(my_list[i])
    list_item = conv_temp(list_item)
    centi.append(list_item)    
    i = i + 1
print(f"Converted List into Fahrenheit: {centi}")






# def conv_temp(cen_temp:int)->int:
#     F:float = float(cen_temp * (9/5) + 32)    
#     return int(round(F,0))
# centi:list = []
# while True:
#     list_item:str = str(input("Add Temperature in Centigrade to List: (Enter 'S' to show in Fahrenheit)  "))
#     if list_item=='S' or list_item=='s':
#         break
#     else:
#         list_item:int = int(list_item)
#         list_item = conv_temp(list_item)
#         centi.append(list_item)
# print (f"After conversion Temperatures in Fahrenheit: {centi}")

