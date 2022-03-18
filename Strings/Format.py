#string method is the method, in which we can combine the strings & numbers:

#example
age = 20 #int as 20 
txt = "My name is Mayuresh, I am {}" 
#format is the method, which takes the passed argument them, and then places them in the string 
print(txt.format(age)) #print the value 

#use index number(0) to be sure when the argument are placed in the correct

quantity = 3
itemno = 729 
price = 100.89 
myorder = "I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity,itemno,price)) 

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

#Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))