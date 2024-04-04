# number = 5 # claim variable int

# # del number  # delete variable
# print(number)
# number = 4 # reclaim variable
# print("Result:", number)

number = 5 # int
digit = 4.56 # float
word = "Some value:" # string
boolean = True # or False boolean
str_num = "456"
print(word, digit) 
print(word * 3) # multiply string (Some value:Some value:Some value:)
print(word, str(digit)) # transform float to string
print(number + int(str_num)) # sum of 5 and 456
print(word + str(number + int(str_num))) # Some value:461
