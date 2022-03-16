#python does not have any so called random() function to call the number in the randomise number 
#but.but. python a module which is also called random()  to call a group of number in the randomize number 

#first step is import the module 
import random

print(random.randrange(1, 10))

"""""
pro tip: dont save the file with the same name of the import term 
it will show you the error something like this 
"AttributeError: partially initialized module 'random' has no attribute 'randrange' (most likely due to a circular import)"
"""