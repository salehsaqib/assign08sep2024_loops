# 5. *Create a function* that takes a positive integer as a parameter and uses a 
# while loop to calculate and return the factorial of that number.

def cal_fact(num:int)->int:
    i:int = num
    while i > 1:
        num = num*(i-1)
        i-=1
    return num
    
num:int = int(input("Enter Number to calculate factorial : "))
print(cal_fact(num))

