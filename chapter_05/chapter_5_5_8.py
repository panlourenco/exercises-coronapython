# 5-8. Hello Admin:

usernames=['admin','josh','karl','peter','marry']
for username in usernames:
    if username=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print('Hello '+ username.title() +', thank you for logging in again.')
