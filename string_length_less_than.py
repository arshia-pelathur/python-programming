input_string = "Arshia Pelathur is 25 years old. She is a Women"

words = [item for item in input_string.split() if len(item) < 5 ]

print(words)