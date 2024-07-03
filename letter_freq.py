def frequency(string):
    chars = set(string.replace(' ',''))
    return {char:string.count(char) for char in chars}

example = 'canada is a cold country'
print(frequency(example))