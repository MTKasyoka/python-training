fruits=['Mangoes','bananas','oranges','lemon','xyz']
for i in fruits:
    print(i)

x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    print(i)

#range ()-used to create a list on numbers 

numbers=list(range(1,100))
print(numbers)
for i in numbers:
    print('Alex')


# create a list of numbers from 10 to 50
#print your name  40 times
numbers=list(range(10,51))
print(numbers)
for i in numbers:
    print('Mwikali')

#check even numbers
numbers=list(range(10,51))
even_numbers=[] #even numbers to be on a list
for  num  in numbers:
    if num%2==0:
        even_numbers.append(num)
        #print(num)
print(even_numbers)

# odd numbers 
numbers=list(range(10,51))
odd_numbers=[] #the odd numbers to be on a list 
for  num  in numbers:
    if num%2!=0:
        odd_numbers.append(num)
#print(num)
print(odd_numbers)

numbers=list(range(10,51))
for  num  in numbers:
    if num%2==1:
        print(num)

# break- used to stop a loop 
numbers=list(range(1,1000))
for i in numbers:
    if i==10:
        break

#Write a program that displays a numbers 1 to 50 inside a list.
numbers=list(range(1,51))
print(numbers)

#From 1 above display the ones divisible by 7 or 5 inside a list.
x=[]
numbers=list(range(1,51))
for r in numbers:
    if r%7==0 or r%5==0:
            x.append(r)
print(x)

#Find sum and average of values in the range between 10 to 40.
numbers=list(range(10,41))
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

sum=0
for i in numbers:
    sum=sum + i
print(sum)


#Put in a list the first 10 odd numbers between 10 to 50. 
numbers=list(range(10, 51))
odd_numbers=[]

for num in numbers:
    if num%2!=0:
        odd_numbers.append(num)
        if len(odd_numbers)==10:
            break

print(odd_numbers)

#odd_numbers = [num for num in range(11, 50) if num % 2 != 0][:10]
#print(odd_numbers)


#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

numbers=list(range(11))
user_input=input('Enter number:')
user_input=int(user_input)
for i in numbers:
    mult=i*user_input
    print(f'{i}*{user_input}={mult}')


#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
numbers=list(range(1,51))
even_numbers=[]
for x in numbers:
    if x%2==0:
        even_numbers.append(x)
print(len(even_numbers))


#Display the total quantity of the 3 above.
ls1 = [ ("Jay", "20") , ("Mo", "30"), ("Mya", "32") ]

total_quantity=0
for i in ls1:
    quantity= int(i[1])
    total_quantity=total_quantity+quantity
    print(total_quantity)






