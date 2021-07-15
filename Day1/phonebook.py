import random

phonebook = {'중국집' : '111-111-1111', '돈까스집' : '222-222-2222', '냉면집' : '333-333-3333'}
print(phonebook)
a = random.choice(list(phonebook.values()))
print(a)