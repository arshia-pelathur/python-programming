fahrenheit = [temp for temp in range(-60,70,10)]

celsius = list(map(lambda ftemp:round((ftemp - 32) *(5/9),2) , fahrenheit))

print('Fahrenheit','Celsius',sep='\t')
for ftemp,ctemp in zip(fahrenheit,celsius):
    print(ftemp,ctemp,sep='\t')
