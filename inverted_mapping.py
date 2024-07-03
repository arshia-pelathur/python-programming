def invert(dictionary):
    i=0
    inverted_dictionary = {}
    for key,value in dictionary.items():
        inverted_dictionary[value] = key
    return inverted_dictionary

sample_dict = {i:'value_'+ str(i) for i in range(1,11)}
print(sample_dict)
print('\n','After Inverted Mapping:')

print(invert(sample_dict))
