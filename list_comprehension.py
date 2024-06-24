input_string = "ArshiaPelathur"

not_vowels = [char for char in input_string if char.lower() not in ['a','e','i','o','u']]

print(not_vowels)