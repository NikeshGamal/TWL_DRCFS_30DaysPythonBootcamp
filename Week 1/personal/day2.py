#control flow statements
#For driving license(Bike):
print('*********driving license*****************')
#1.input user's age 
age_str = input("What is you age? ")

#2.conver user's age to integer
age = int(age_str)

#3.check user is older than 16 years old
#4.if user is older, show he is eligible else show he is not
#comparing user's age
if age >=16:
    print('You are old enough to drive a bike')
else:
    print("Your are not old enough to drive a bike")
print('************************************')

print("************Login System************************")
username=input("Enter your username: \n")
password = input("Enter your password: \n")

if username == 'nikesh_gamal' and password=='gamalnikesh':
    print(f'Welcome {username} you are successfully logged in')
elif username == 'admin' or password == 'admin':
    print(f"Welcome {username} to admin Panel")
else:
    print('Invalid Credentials! Please Enter valid credentials')


#***********Looping statement******************
# doing multiple works with slight changes-->loop

#for loop-----> if we know number of loop to be run
#while loop------> if we dont know how many times loop is going to be run

#-----------for loop------------------
#first ko kura lai include garxa but last ko kura chai exclude hunxa
for i in range(5,11):
    print(i)


# Range Function:
# 1.range(1,10)-->0,1,2,3,4...9
# 2.range(1,11)-->1,2,3,4...10
# 3.range(10,1,-1)-->10,9,8,....2


#print odd number from 1 to 10
print("Odd number:")
#for i in range(0,11,2) // last parameter indicates jumping of steps while looping
for i in range(11,0,-1):
    if i%2!=0:  # %-->called modulo operator that returns remainder
        print(str(i) + " is odd")
    #if you are concantenating using + then convert integer to string
    else:
        print(i,"is even")
    #if we are using , no need to convert integer
