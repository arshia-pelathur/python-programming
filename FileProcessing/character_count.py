import os
from os import strerror,getcwd



path = os.path.dirname(__file__)

filename = open('.\\FileProcessing\\characters.txt','w')
filename.write('bcdBCDabCDaaBBBBBcDD')
filename.close()

def count(content):
    chars = ''.join(set([item.lower() for item in content]))
    i=0
    countdict = {}
    while i<len(chars):
        countdict[chars[i]] = content.lower().count(chars[i])
        i+=1
    return countdict
        
def print_counts(data):
    for key,value in data.items():
        print(key,value,sep='->')

srcname = input('Enter the file name: ')
try:
    with open(path+'\\'+srcname,'r') as f:
        content = f.read()
        print('Frequency of characters in file')
        countdict = count(content)
        print_counts(countdict)
        
        print('Sorted Dictionary')
        sorted_values = dict(sorted(countdict.items(),key = lambda value:value[1],reverse = True))
        print_counts(sorted_values)
except IOError as err:
    print('Not specified file. ERROR NUMBER: ',err.errno,'\n' + strerror(err.errno))
    
