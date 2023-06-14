print ('\033[1;35m find out the details of the inserted variable STR')
word = (input ('\033[1;34m enter the variable:\n'))
count = 0
print ('\033[4;34m what is type of the variable ? \n', type(word))
print ('\033[4;31m is only spaces? \n', word.isspace())
print ('\033[4;32m How many spaces does the variable have?')
for a in word:
    if (a.isspace()) == True:
        count+=1
print (count)
print ('\033[4;34m how many character have the variable? \n', len(word))
print ('\033[4;31m it`s just letters ? \n',word.isalpha())
print ('\033[4;32m contains only numbers ?\n', word.isnumeric())
print ('\033[4;34m is alphanumeric? \n', word.isalnum())
print ('\033[4;31m is it in capital letters? \n', word.isupper())
print ('\033[4;32m it`s in lower case ? \n', word.islower())
print ('\033[4;33m the first letter this in capitalized ? \n', word.istitle())



