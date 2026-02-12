# creating a programme that gonna check a password
# first we gonna define a predefine password and ask the user to enter it
# if the user attempt 3 times with the wrong password we goimg to display a message 
# telling them they wrong every time and block the programme at the third attempt

max = 3

def password_checking():
    correct_user_name = "python"
    original_password = "54ge4ye44"
    counter = 0

    while counter < max:
        username = input("please enter the username:")
        password = input("please enter the pasword:")

        if username == correct_user_name and password == original_password:
            print("user name and password is correct")
            return
        else:
            counter += 1
            print("username and password are incorrect, try again")
        
    print("you've reachead the maximum attempt")

password_checking()

    
    
