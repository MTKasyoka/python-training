def hello():
    print('Hello world')

hello()

#calculate area of a triangle 

#base=10
#height=6
#area=1/2*base*height
#print(area)

def area_triangle():
    base=10
    height=6
    area=1/2*base*height
    print(area)

area_triangle()


#calculate the area of a circle

def  area_circle():
    r=14
    pie=3.14
    area=pie*r**2
    print(area)

area_circle()

#square_number(num)
#prints the square of a number 
#example: square_number(4)-16

def square_number(l):
    square=l**2
    print(square)
square_number(4)
square_number(5)
square_number(6)
#cube_number(num)
#prints the cube of a number

def cube_number(l):
    cube=l**3
    print(cube)

cube_number(3)
cube_number(5)

#add_numbers (a,b)
#sum=sum+no.
def add_numbers(a,b):
    sum=a+b
    print(sum)

add_numbers(10,30)

#Write a Python Function that checks if a variable password is equal to the string "secret123". If it is, print "Access  "granted", otherwise print "Acess denied"

def correct_password(password):
     check_password='secret123'
if 'user_password'=='check_password':
    print('Acess granted')
else:
        print('Acess denied')

correct_password(12223)

print("Something new")