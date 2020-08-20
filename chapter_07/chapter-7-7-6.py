# 7-6. Three Exits:



loop = 0
while True:
    loop += 1
    message = input("\nPlease enter your age: \n")
    if message == 'quit':
        print (str(loop))
        break
        
    else:
        if (int(message) < 3):
            print("\nYour ticket is free! \n")
        elif(3<=int(message)<=12):
            print("\nYour ticket is $10 \n")   
        else:
            print("\nYour ticket is $15 \n")  


