text_1 = input()
vowels = ['a','o','u','e','i']
new_string = [x for x in text_1 if x.lower() not in vowels]
print(''.join(new_string))