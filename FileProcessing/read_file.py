import os

print(f"Current working directory: {os.getcwd()}")

try:
    count = 0
    with open('.\\FileProcessing\\somefile.txt', 'r') as s:
        file = s.read()
        for char in file:
            print(char,end='')
            count+=1
        print(f'\nNumber of characters in the text file is {count}')
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e} ---> Error Number {e.errno}")
except PermissionError as e:
    print(f"PermissionError: {e} ---> Error Number {e.errno}")
except IOError as e:
    print(f"IOError: {e} ---> Error Number {e.errno}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
