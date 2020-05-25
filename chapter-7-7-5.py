# 7-5. Movie Tickets:

active = True
while active:
    message = input("\nPlease enter your age: \n")
    if message == 'quit':
        active = False
        
    else:
        if (int(message) < 3):
            print("\nYour ticket is free! \n")
        elif(3<=int(message)<=12):
            print("\nYour ticket is $10 \n")   
        else:
            print("\nYour ticket is $15 \n")  


