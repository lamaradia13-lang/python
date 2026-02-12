max = 3

def password_checking():
    correct_user_name = "python"
    original_password = "54ge4ye44"

    for i in range(max):
        username = input("please enter the username: ")
        password = input("please enter the password: ")

        if username == correct_user_name and password == original_password:
            print("user name and password is correct")
            return
        else:
            print("username and password are incorrect, try again")

    print("you've reached the maximum attempt")

password_checking()
