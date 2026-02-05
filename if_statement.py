if 20>10:
    print('yes')
else:
    print('no')

#print 50 is greater if 10 is less than 50
if 10<50:
    print('50 is greater')
else:
    print('odd')

#check if number is even
number=10
if number%2==0:
    print('even number')
   
else:
    print('odd number')


#check if number is odd
number=10
if number%2!=0:
    print('odd number')

if  number%2==1:
    print('odd number')
    

#every odd number divide by 2 remainder will be 1 

#password=input('Enter your password')
#correct_pass='@admin123'

#if password==correct_pass:
    #print


#check if age is greater or equal to 18 print Adult otherwise print minor
age=30
#age=input('Enter your age:')
#age=int(age)

if age>=18:
    print('Adult')
else:
    print('minor')

#check if marks is greater than 80 print grade A, if marks is 70 to 80 print grade B,  if marks is 60 to 69 print grade C, if marks is 50 to 59  print grade D otherwise print Grade E
marks=60

if marks>80:
    print('grade A')
elif  70<= marks<=80:
    print('grade B')
elif 60<=marks<=69:
    print('grade C')
elif 50<=marks<=59:
    print('grade D')
else:
    print('grade E')


#Take three inputs from a user, separately. Print the largest of the numbers.
   # Hint: Determine what type of data is taken in as input.
num1=input('Enter Number one:')
num1=int(num1)
num2=input('Enter Number two:')
num2=int(num2)
num3=input('Enter Number three:')
num3=int(num3)


if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

#formatted String- used to display variables in strings , variables must be inside {} and start with f before quotations.


#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”



#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"



#5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

#Take four inputs from a user, separately. Print the largest of the numbers.

num1=input('Enter Number one:')
num1=int(num1)
num2=input('Enter Number two')
num2=int(num2)
num3=input('Enter Number three')
num3=int(num3)
num4=input('Enter Number four')
num4=int(num4)

if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is the largest")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is the largest")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3}is the largest")
else:
    print(f"{num4} is the largest")
















    
#Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".






#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".


#3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
#Prints "Access Granted" if user_id is in valid_ids.
#Prints "Access Denied" if user_id is not in valid_ids.



#4.Given a variable value that could be of any type, write a conditional statement that:
#Prints "String Detected" if value is a string.
#Prints "Integer Detected" if value is an integer.
#Prints "Unknown Type" for any other type.



#5.Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.
