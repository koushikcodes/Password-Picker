import random
import string

adjectives = ['sleepy', 'slow', 'smelly',
 'wet', 'fat', 'red',
 'orange', 'yellow', 'green',
 'blue', 'purple', 'fluffy',
'white', 'quick', 'brave', 'enigma']

nouns = ['apple', 'kitty', 'ball',
 'toaster', 'goat', 'dragon',
 'hammer', 'duck', 'panda']

print('Welcome to Password Generator__**made by ANONWIZ**')

while True:
   adjective = random.choice(adjectives)
   noun = random.choice(nouns)
   number = random.randint(0, 100)
   special_char = random.choice(string.punctuation)
   password = "".join([adjective,noun,str(number),special_char])
   print('Your new password is: {}'.format(password))
   response = input('Would you like another password? Type y or n: ')
   if response == 'n':
   	break
