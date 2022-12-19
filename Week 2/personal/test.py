# #1.error handling
# #1.input --> username ,password
# #csv-->     comma separated values
# #O/p: nikesh,gamalnikesh
# #----> join(" ")--->return string  split()-->list      string ko methods index,remove,count

# #join()--->username password--> mini shah
# # ','.join((username,password))

# #error handling
# """
#  try:
#     code
#     if error sanga encountered
#     goes to except
# except type_of_error:  specidfic thaha xaina bhane __Exception as e
#     code
# """
# status=True
# while status:
#     try:
#         filename= input("enter the file path: ")

#         with open(filename,"r") as file:
#             contents = file.read()
#             print(contents)
#         status=False
#     except FileNotFoundError:
#         print("No such file or directory")

# #input--username password ---kunaiyeuta file ma write garnu paryo csv--> username,password

#slice--->paper cutting 

#for eg:  n ike sh  ike

# name ="Chandramukhi" #o/p--> chandra
# #syntax: [starting_index: end_index]---> starting_index(inclusive) and end_index(exclusive)
# res=name[0:7]
# print(res)

#1.file read, file write, join, split, slice , list comprehension

#list _comprehension
# sum=0
# # for ind in range(0,5): #[0,1,2,3,4]
# #     sum =sum+ind

# # sum = [print(sum+ind) for ind in range(0,5)]

# print(sum)
# 

# any() all()

# or---> if any of the condition is true then True
# and--> if all of the conditions are true only then True

# any-->or
# all-->and

#1. name --> if any small letters xa bhane print there is lowercase letters
#2. name--> if all uppercase letters ho bhen print all the letters are in uppercase

name="MINI"

#loop
status = False
for ch in name:
    print(ch)
    #if encountered with lower case then change status to True
    if True:
        status = True
    
def has_lower(name):
    return True if any([ch.islower() for ch in name]) else False  #ternary operator

if status:
    print("There is atleast one lowercase letters")
else:
    print("There are no any lowercase letters")

# any([True,False,True])-->True
# all([[True,False,True]])---->False
# all([True,True,True])-->True


import string
list_special = list(string.punctuation)
print(list_special)

user_input = "pokhara#$@"
# for ch in user_input:
#     if ch in list_special:
#         print(f"{ch} is special character")

mylist=[ch if ch in list_special else "" for ch in user_input]
print(mylist)
'''
  gamal123--> a-True b-False c-False d-true

 .islower() .isupper() .isdigits()
'''

#1.take input ask from user then 
#a.contains lowercase or not
#b. contains uppercase or not
#c. contains special character or not
#d contains numbers or not