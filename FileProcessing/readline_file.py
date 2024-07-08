
try:
    c = 0
    char = 0
    with open('.\\FileProcessing\\dandelions.txt','r') as file:
        line = file.readline()
        while line!='':
            print(line)
            c +=1          # counting number of lines
            char+=len(line)
            line = file.readline()
        print(f'Number of characters: {char}')
        print(f'Number of lines: {c}')
except IOError as e:
    print(f'{e}')