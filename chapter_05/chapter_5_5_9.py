# 5-9. No Users:

usernames=[]
if usernames:
    for username in usernames:
        if username=='admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print('Hello '+username+',thank you for loging in again.')
else:
    print("We need some users.")