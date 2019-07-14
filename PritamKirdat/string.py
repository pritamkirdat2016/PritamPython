mystr = 'Hello Word'

cnt = mystr.count('H') #counting occurance of 'H' in mystr return type integer

mystr.istitle() #checking for string is in format of Title returns true/False (boolea)
mystr.lower # convert string to lower case and return to that string

 
mystr.find('w') # finding for 'w' in string if not found it returns -1 and
#if it found the returns its index output for this -> 6

newStr = mystr.index('d') # return index of given workd in string
print(newStr) # output is 9


newStr = mystr.upper() # convert string to upper case and return that string
print(newStr) # 'HELLO WORD!'

mystr = ' Hello Word  '
print(mystr) #' Hello Word  '
newStr = mystr.lstrip() # remove space from leftside of string and return the string
print(newStr) # 'Hello Word  '

newStr = mystr.rstrip() # remove all space from right side of string and return the string
print(newStr) #' Hello Word'

newStr = ' Hello Word! 123'
print(newStr.isnumeric()) #returns Boolean value, True when string is numeric else false
#False
newStr = '123'
print(newStr.isnumeric())#True

newStr.isalpha() #Returns False when string is alphabates else return false
 newStr = 'ABC'
print(newStr.isalpha())# True

