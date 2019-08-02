# Python3 code to demonstrate 
# Filling alphabets 
# using naive method 

# initializing empty list 
test_list = [] 

# printing initial list 
print ("Initial list : " + str(test_list)) 

# using naive method 
# for filling alphabets 
alpha = 'a'
for i in range(0, 26): 
	test_list.append(alpha) 
	alpha = chr(ord(alpha) + 1) 

# printing resultant list 
print ("List after insertion : " + str(test_list)) 
