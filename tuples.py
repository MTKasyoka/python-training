students=('Alex','James','Mike','Mary','John')
print(type(students)) #tuple
print(students)

#display James -We use index
print(students[1])

#display Mary
print(students[3])

#change mary to Juma
#We cannot change since Tuples are immutable 
#convert a tuple to a list using list()- #modify list-covert back to tuple using tuple()

students=list(students)
students[3]='Juma' #modify

#convert to tuple using tuple()
students=tuple(students)
print(students)
print(type(students))



#add your name between Alex and Jane
students=list(students)
students.insert(1,"Mwikali")
students=tuple(students)
print(students)
print(type(students))


days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
print(days[2])

#2. Using a function a find the length of the tuple.
print(len(days))

#3. Replace Thursday with Thur
days=list(days)
days[3]='Thur'
days=tuple(days)
print(days)
print(type(days))


numbers=(10, 20, 30, 40, 50)
#Add 60 to the end
numbers=list(numbers)
numbers.append(60)
numbers=tuple(numbers)
print(numbers)

# Replace 30 with 35.

numbers=list(numbers)
numbers[2]=35
print(numbers)
numbers=tuple(numbers)

values = (15, 5, 30, 25, 10) 
#arrange the elements in ascending order.
values=list(values)
values.sort()
values=tuple(values)
print(values)

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",
fruits=list(fruits)
print(fruits.count('banana'))

# Remove all occurrences of "banana"
fruits=list(fruits)
fruits.remove("banana")
fruits.remove("banana")
fruits.remove("banana")
#fruits [1] [3] [5].remove("banana")
#del fruits [1] [3] [5]
#fruits [1] [3] [5].pop()
print(fruits)

names = ("Alice", "Bob", "Charlie", "David") 
#Reverse the order of elements using sort method.
names=list(names)
names.sort(reverse=True)
names=tuple(names)
print(names)

colors = ("red", "blue", "green")
colors=list(colors)
colors.sort(reverse=True)
print(colors)
colors=tuple(colors)

#add "yellow" at index 1,

colors=list(colors)
colors.insert(1,'yellow')
colors=tuple(colors)
print(colors)

# Extend with ["purple", "orange"]
colors=list(colors)
my_colors= ["purple", "orange"]
colors.extend(my_colors)
print(colors)
