# Python3 code to demonstrate working of 
# Finding min value keys in dictionary 
# Using min() + list comprehension + values() 
  
# initializing dictionary 
test_dict = {'physics' : 88, 'maths' : 75, 'chemistry' : 72, 'basic electrical':89} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# Using min() + list comprehension + values() 
# Finding min value keys in dictionary 
temp = min(test_dict.values()) 
res = [key for key in test_dict if test_dict[key] == temp] 
  
# printing result  
print("Keys with minimum values are : " + str(res))
