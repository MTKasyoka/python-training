#check type of each  variable  print(type(value)), Note that the value is the name of the variable which contains the data 
#string- has a quotation 
my_name="Mwikali Kasyoka"
print(type(my_name))

#interger-numerical character not in a quotation
num1=200
print(type(num1))

#float-numeric character with a decimal point and not in a quotation
num2=99.56
print(type(num2))

#boolean- true/false
value=True
print(type(value)) 


#strings concat when you add them 
#quotation are used to create space 
#syntax- nv3=nv1+""+nv2
first_name="Mwikali"
last_name="Kasyoka"
full_name=first_name+" "+last_name
print(full_name)

#indexing- characters in a string have numerical representation. Index are given on square brackets [].
#syntax - print(nv[No.])
#from the left you start with 0. From the right you start -1.

sentense1="My name is Mwikali Kasyoka and I am a Software Developer"
print(sentense1[38])
print(sentense1[-18])

#when the value has a quotation, use double quotations.
sentense3="I'm a python Student"
print(sentense3[6])

#slicing - extracting a part of a string. We use indexing for slicing
#syntax - print(nv[start index:end index+1])
print(sentense3[6:20])
print(sentense3[0:12])

