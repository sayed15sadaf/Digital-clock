#how to create a list// WAP to demonstrate the concept of list
'''
list1=["C","C++","Java", "Python", "C#"]
print(list1)
for i in list1:
 print(i)
'''

'''
list1=[]
list1.insert(0,"C")
list1.insert(1,"Python")
print(list1)
'''

'''
# WAP to create a list of 5 numbers: 
list1=[] # Empty List
for i in range(5):
 n=int(input(f"Enter the {i+1} Element: "))
 list1.insert(i,n)
print(f"The Elements in the list are {list1}")
'''


'''
# Sort a list in ascending order:-
list1=[4,5,10,2,8] #Given elements
list1.sort() #Elements sorted in ascending order
print(list1) #sorted list will be printed
'''


'''
list1=[]
for i in range (7):
 l=int(input(f"Enter the {i+1} Element of the list: "))
 list1.insert(i,l)
list1.reverse()
print(f"The reversed inserted elements are {list1}")
'''


'''
#WAP to create a list of 5 numbers by user input and display numbers in ascending and descending order
list1=[]
for i in range (5):
 l=int(input(f"Enter the {i+1}st Element of the list: "))
 list1.insert(i,l)
list1.sort()
print(f"The ascending inserted elements are {list1}")
list1.reverse()
print(f"The descending inserted elements are {list1}")
'''

'''
#WAP to find maximum value, minimum value, sum of the values and length of the list
list1=[10,20,30,40,50]
print (list1)
print(f"Length of list = {len(list1)}")
print(f"Sum of value of list = {sum(list1)}")
print(f"Maximum value in list = {max(list1)}")
print(f"Minimum value in list = {min(list1)}")
'''

#WAP to store 5 names in list by user input now display names in alphabetical order.

list1=[]
for i in range (5):
 l=(input(f"Enter the {i+1} Element of the list: "))
 list1.insert(i,l)
list1.sort()
print(f"The names in alphabetical order are {list1}")
























