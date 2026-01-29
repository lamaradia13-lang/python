# creating a function that's going to check if a user password is strong enough or not
# first I'm going to ask the user to enter his or her password, after getting it I'm
# going to run it through by calling the function. and then I'll return a message telling
# if the password is strong enough or not using print.

def checkin_password():
    password = input('please enter your password:')
    if len(password) < 12:
        return "the password is not long enough"
    if password.isdigit():
        return "your password only contains numbers!"
    if password.isalpha():
        return "your password only contains letters!"
    if not any(not c.isalnum() for c in password):
        return "your password must contain at least one special character"
    else:
        return "your password is secured!"


checking = checkin_password()
print(checking)
