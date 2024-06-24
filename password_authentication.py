import time


def check_information(uname,pword):

    correct_username = 'ArshiaPelathur'
    correct_password = "EverythingEverywhereAll@Once"
    return correct_username == uname and correct_password == pword


def main():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if check_information(username,password):
            print('Correct Credentials. \nAccess Granted')
        else:
            attempts-=1
            print('Incorrect username or passwword. Please try again')
    print("Access Denied after 3 failed attempts. Please try again in 60 mins")
    
    time.sleep(3600)  # Wait for 60 minutes 
    print("You can now try again.")
    main()

if __name__ == '__main__':
    main()