num1=1000
num2="2000" #you change the string to an integer using the int() function 
#int()-Its a function. Convert a numerical string and float into an integer 
num2=int(num2)
print(type(num2)) #type used to show what the type of variable is 
num3=num1+num2
print(num3)

#int function used to convert a float to an integer 
num4=99.7564 
print(int(num4))

#
num5=round(num4,1)
print(num5)




#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
temp=56.8926
print(int(temp))


#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 

temp=56.8926
print(round(temp,2))

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
temp=56.8926
print(round(temp,3))

#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 
#convert to a string-slice-concatenation-float 
temp=56.8926
temp=str(temp) #print(type(temp))
temp=temp[3:7] #8926
temp=temp[0] + "." + temp[1:4]
temp=float(temp)
print(temp)

#convert 56.8926 to 5.6 
#string-slice-concantenation-float 


