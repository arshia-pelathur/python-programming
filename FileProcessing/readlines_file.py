from os import strerror

try:
    ccnt = lcnt = 0
    s = open('.\\FileProcessing\\dandelions.txt', 'rt')
    lines = s.readlines()
    print(lines)
    value = 0
    print(lines[value])
    while len(lines[value]) != 0:
        lcnt += 1
        print(lines[value],end='')
        ccnt += len(lines[value])
        value+=1
        if value>=len(lines):
            break
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
