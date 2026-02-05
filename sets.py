numbers={10,20,30,40,50,10,40,50}
print(numbers)
print(type(numbers))

#sets only store unique values- the output will not display the repeated numbers

#Methods 

#add()-used to add numbers
numbers.add(1000)
print(numbers)

#remove-used to remove items in a set - remove a no. that is not there you get an error
numbers.remove(10)
print(numbers)

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

#Remove friday and sunday from the set using methods.

days.remove('friday')
days.remove('sunday')
print(days)

#Add them back to the set

days.add('friday')
days.add('sunday')
print(days)
