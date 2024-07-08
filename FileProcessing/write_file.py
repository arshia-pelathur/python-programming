try:
    newfile = open('.\\FileProcessing\\stars.txt','w')
    for i in range(10):
        newfile.write('*')
        for j in range(i):
            newfile.write('*')
        newfile.write('\n')
    for i in range(j+1,0,-1):
        for k in range(i):
            newfile.write('*')
        newfile.write('\n')
    newfile.close()
except IOError as exp:
    print('I/O Error occurred as ',exp)