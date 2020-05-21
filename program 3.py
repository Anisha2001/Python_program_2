# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [1,2,3,4,5,6,7] 
list2 = []   
for num in list1:
    if num % 2 == 0: 
       list2.append(num)
       list1.remove(num)
print(list1)
print(list2)
        
