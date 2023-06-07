print ('find out the details of the inserted variable STR')
word =  (input ('enter the variable:\n'))
count = 0
print ('what is type of the variable ? \n', type(word))
print('is only spaces? \n', word.isspace())
print ('How many spaces does the variable have?')
for a in word:
    if (a.isspace()) == True:
        count+=1
print (count)
print

