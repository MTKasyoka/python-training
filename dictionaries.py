#create a dictionary 
my_dict={
        'name': 'Ropy Kevin',
        'city':'Nairobi',
        'age': 25,

           }
print(my_dict)
print(type(my_dict))

# displaying valus in a dictionary - use the key
#display Nairobi 
print(my_dict['city'])

#name-Ropy Kevin 
print(my_dict['name'])

#  age-25
print(my_dict['age'])

#adding items- the item is added to the last item 
my_dict['occupation']='software developer'
my_dict['skills']=['reseacher','graphic designer','video editing']
#display skills 
print(my_dict['skills'])
#display graphic designer 
print(my_dict['skills'][1])

#updating values- Keys are case sensitive 
#age -30 
my_dict['age']=30
print(my_dict)

#update city 
my_dict['city']='Kisumu'
print(my_dict)

# contact
my_dict['contact']=567889
print(my_dict)

#Dictionary methods 
#remove specific items 
#.pop()- remove a specific key 
my_dict.pop('age')
print(my_dict)

#.popitem()- removes the last item 
#my_dict.popitem()
print(my_dict)

# .values()- used to display a list of only values in a dictionary
print(my_dict.values())

#.keys()-used to display a list of only keys in the dictionary
print(my_dict.keys())

#.items()-used to disply a lst of all items in tuples 
print(my_dict.items())

#.get(key)- used to get values in a dictionary
print(my_dict.get('city'))


my_ds = [23,'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987, (76,'John')]
#1. Print KES
print(my_ds [3][2] ['currency'])

#2. Print 560
print(my_ds[2])
#3. Print Maths
print(my_ds[3] [1])
#4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3] [2] ['amount']=90
print(my_ds)
#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
     #Hint: Strings can be reversed using [::]

     
#6. Change the name “John” to “Jane” . 
