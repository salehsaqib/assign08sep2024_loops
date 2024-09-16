# 2. *Implement a simple shopping cart program* using an array. 
# Create functions to add items, remove items, and update quantities using array methods. 
# Print the cart's contents after each operation.
def add_item(ulist:list,uval:str):
    ulist.append(uval)    

def del_item(ulist:list,uval:str):
    ulist.remove(uval)    

def show_cart():
    print("------------------------------Current Cart----------------------------------")
    i:int = 1
    for x in ulist:
        print(f"{i} : {x}")
        i+=1
    
    

ulist:list = []
show_cart()
print("---------------------------Select Cart Operation (Below) --------------------")
list_op:str = str(input("Enter A for Add - D for Delete - U for Update - Q for Quit : "))

while True:
    if list_op=='A' or list_op=='a':
        cart_prd:str = str(input("Enter Product to add in the cart : "))
        add_item(ulist, cart_prd)
        show_cart()
        print("---------------------------Select Cart Operation (Below) --------------------")
        list_op:str = str(input("Enter A for Add - D for Delete - U for Update - Q for Quit : "))
    elif list_op=='D' or list_op=='d':
        cart_prd:str = str(input("Enter Product to delete from the cart : "))
        del_item(ulist, cart_prd)
        show_cart()
        print("---------------------------Select Cart Operation (Below) --------------------")
        list_op:str = str(input("Enter A for Add - D for Delete - U for Update - Q for Quit : "))
    elif list_op=='U' or list_op=='u':
        old_prd:str = str(input("Enter Product to Update/Replace from the cart : "))
        new_prd:str = str(input("Enter New Product to Update in the cart : "))
        del_item(ulist, old_prd)
        add_item(ulist, new_prd)
        show_cart()
        print("---------------------------Select Cart Operation (Below) --------------------")
        list_op:str = str(input("Enter A for Add - D for Delete - U for Update - Q for Quit : "))
    else:
        break