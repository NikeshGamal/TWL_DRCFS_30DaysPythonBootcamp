#FIZZ-BUZZ 
#Program Details:
#divisible by 3 --> print Fizz
#divisible by 5 --> print Buzz
#divisible by both 3 and 5 --> FizzBuzz
#divisible by none --> print the number as it is

#Solution

#1. generate a number and take input --> use loop
#2.check which condition which one satisfied

for i in range(1,11):
    if i % 3 == 0 and i % 5==0:
        print("*"*40)
        print(f"{i}-->FizzBuzz")
        print("*"*40)
    elif i % 3==0:
        print("*"*40)
        print(f"{i}-->Fizz")
        print("*"*40)
    elif i % 5 == 0:
        print("*"*40)
        print(f"{i}-->Buzz")
        print("*"*40)
    else:
        print(f"Your number is {i} which is not divisible by neither of the value")