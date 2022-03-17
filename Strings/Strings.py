"""
Strings are surronded by the 'single quotation marks', "double quotation mark" 

for Example: 
    'hello guys' or "Hello Guys"
    Print the values using [ "print()" ]
"""

print("hello")
print('hello')


#assign the values to string 
a = "hello"
print(a)

#multiline Strings (three double quote)
b = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(b)

#multine String (three single quote)
c = ''' Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua boy. '''
print(c)

#strings are arrays 
#strings in Python are arrays of bytes representing unicode characters

v = "mayuresh" 
#Square brackets can be used to access elements of the string "[]" 
print(v[1])

#looping the variable through a string
#by using "for" > loop 

for x in "straight": 
    print(x)

#String Length 
#use this method to get the length of the string 
#we use the "lens()" > functions

#example 
a = "Mayuresh"
print(len(a))

#string are the the phrase or a character which is present in a string, 
#so we can use the keyword is "in"

txt = "I love to play God of war" 
print("free" in txt)
#it will state in the true or false method

#use it in an "if" method
#use this method you want to check any word is there or not 
txt = "the best thing is doing me is now" 
if "right" in txt: 
    print("yes,'right' is present")
    #there is not ant "right" word so it will not print in the output 

#CHECK if NOT
#to check a certian a word is avaliable or not in the keyword or not there 
#for that we will use "not in" 

txt = "the best thing is not always free!"
print("costly" not in txt) 


#Use it in an if statement:

#Example
#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
