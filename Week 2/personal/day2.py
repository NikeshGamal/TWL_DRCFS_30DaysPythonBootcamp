#function

#if there repetitive code --> it is better to use function (maintainability)


#to define a function we use def keyword and use : to indicate the funciton block followed by the space(1 tab)

#can pass the any value  as parameter

#return simply return the result as a result of the function call 
  #later --> it can be saved to a varibale and can be used 

def square_num(num):
    num=num*num
    return num

def add_one(num):
    num = num+1
    return num

def greet(name):
    print(f"Hello {name}")

greet("Nikesh")

num = int(input("Enter a number?: "))
square_number= square_num(num)
print("-"*40)
print(f"The square number of {num} is {square_number}")
print("-"*40)
add_one_number = add_one(square_number)
print(f"Addtion of one to square number {square_number} is {add_one_number}")
print("-"*40)


# print the value for function x^2+2*x+1

def func(num):
    result = num**2+2*num+1
    return result

print("-"*40)
func_value = func(num)
print(f"The value of the function for value {num} is {func_value}")
print("-"*40)

def cubic_number(num):
    return num**3

#calling funciton inside print 
print(f"The cubic value of number {num} is {cubic_number(num)}")
print("-"*40)

# print(cubic_number(2)+cubic_number(3))

print()
#-----------multiple argument--------
#parameters will only valid inside the block of function only

def details(name,age):
    return f"Hello! I am {name}. I am {age} years old"

print("-"*40)
personal_details = details("Nikesh Gamal",22)
print(personal_details)
print("-"*40)
print(details("Mini Shah",21))
print("-"*40)
