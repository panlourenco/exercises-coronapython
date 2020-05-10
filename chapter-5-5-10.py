# 5-10. Checking Usernames:

current_users=['a','b','c','d','e','h']
new_users=['A','b','f','g','p']
for new_user in new_users :
    if new_user.lower() in current_users:
        print("You should enter another name.")
    else :
        print("This name is available.")