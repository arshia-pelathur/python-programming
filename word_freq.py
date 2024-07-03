def frequency(string):
    words = set(string.split(' '))
    word_count = {word:string.count(word) for word in words}
    return word_count

sample = "How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as \
    he could, and chuck as much wood as a woodchuck would if a woodchuck could chuck wood"

print('\n',frequency(sample))