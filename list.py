my_list=['mangoes', 'oranges', 'bananas', 100,20, 99.67,True,False]

print(my_list)

#finding out the type of list 
print(type(my_list))

# use index to display false
print(my_list[7]) #false

#display 20 #use index
print(my_list[4])

#display oranges to 20 # slice
print(my_list[1:5])

#TASK: Create a List of days of the Week. Print the day today using an index.

days_week= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days_week[2])

list1= [10,20,30,['alex', 'mike', [100,200,800,['a', 'e','i'],'brian']], 40,50,['mary',['kevin','david'],'jane'],60,70]

print(list1[4])

#display i
print(list1 [3][2][3][2])

#display david

print(list1[6][1][1])

#list of operations
#update an item 

content=['mon','tue','wed','thur','fri']
content[1]='tuesday'
content[3]='jan'
content[4]='friday'
print(content)


#list of methods 
#methods of  functions inside a class 
#.append (element)-used to add elements at the list 
content=['mon','tue','wed','thur','fri']
content.append('sat')
content.append('sun')
print(content)

#extend-used to extend a list with another 
numbers=[10,20,30,40]
my_numbers=[50,60,70,80]
numbers.extend(my_numbers)
print(numbers)
#numbers.append(my_numbers)-it is going to add a list

trainees = ["John", [2, ["James","Mary"]]]
#1. Display 2 from the list.
print(trainees[1][0])

#2. Output James  from the list.
print(trainees[1][1][0])

#3. Using a method add 56 at the end of the list.

trainees.append("56")
print(trainees)

#4. Using a method add the name Mike between James and Mary
trainees [1] [1].insert(1,"Mike")
print(trainees)

#5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#6. Remove John and Mary from the list.
trainees.remove("John")
#del  trainees[0]
#trainees.pop(0)
trainees [0] [1].remove("Mary")
#you can use pop()- trainees [0] [1].pop()
# del trainees [0] [1] [2]
print(trainees)

#7. Using a function, determine the length of the list
print(len(trainees))

