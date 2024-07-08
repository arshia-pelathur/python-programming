data = bytearray(10)
print(data)
print(len(data))
data[5] = 255

for b in data:
    print(bin(b))