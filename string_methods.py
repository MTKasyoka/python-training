# .upper()- capitalize & .lower() -loowercase
myname="Mwikali Kasyoka"
#print(myname.upper())
myname=myname.upper()
print(myname)
myname=myname.lower()
print(myname)

#.strip()-removes space from start and end of string 
x="       Python Programming "
#print(x.strip())
x=x.strip()
print(x)

#clean full_name "   rOPy KEVin   " to " ropy kevin"
full_name="   rOPy KEVin   " 
#print(full_name.strip().lower())
full_name=full_name.strip()
full_name=full_name.lower()
print(full_name)

#replace- replaces character in a string. Can also be used to delete characters in a string.
#syntax- nv=nv.replace('old','new')
myname="Ropy Kevin"
myname=myname.replace('Kevin','Alex')
print(myname)

#delete character
#syntax- nv=nv.replace('K','')
myname="Ropy Kevin"
myname=myname.replace('K','')
print(myname)

#clean text= "    PyTHon  PROGraMming    " into  "JAVA PROGRAMMING"

name= "   PyTHon  PROGraMming   "
name=name.strip()
name=name.upper()
name=name.replace('PYTHON','JAVA')
print(name)

#split- split a string using a certain character within the string forming a list 
text="I am a python student"
print(text.split())
text="I am a python, student"
print(text.split(','))
text="I am a; python; student"
print(text.split(';'))

#count()- It counts the number of appearances of a character.
text="I am a python, student"
print(text.count('a'))
print(text.count('i'))

#len()- its a  function. Used to count all the characters in a string.
text="I am a python student"
print(len(text))


#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
name="   JOHn  ."
name=name.strip()
name=name.lower()
name=name.replace('.','')
print(name)

#Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”

sentence_one='The Dog Breed is German Shepherd'
sentence_one=sentence_one.replace('The Dog Breed is German Shepherd','Breed is German')
print(sentence_one)

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”

sentence_two='Defeats for the Clinton forces, this was her moment of triumph'
sentence_two=sentence_two.replace('Defeats for the Clinton forces, this was her moment of triumph','Clinton forces')
print(sentence_two)


#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
animal='The lazy dog; ran so fast; it hit the wall.'
print(animal.split(';'))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name= "   Joh.n  "
first_name=first_name.strip()
first_name=first_name.replace('.','')

last_name="   Do,e"
last_name=last_name.strip()
last_name=last_name.replace(',','')
full_name= first_name+ " " + last_name
print(full_name)


#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r= '["E","W","C"]'
print(r[3:9:15])


