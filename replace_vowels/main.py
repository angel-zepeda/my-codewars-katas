vowels = ['a', 'e', 'i', 'o', 'u']
string = 'angel'

string_splitted = ''.join(list(word for word in string if word not in vowels))

print(string_splitted)
