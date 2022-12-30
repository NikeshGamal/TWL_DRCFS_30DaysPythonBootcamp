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

# name="MINI"

# #loop
# status = False
# for ch in name:
#     print(ch)
#     #if encountered with lower case then change status to True
#     if True:
#         status = True
    
# def has_lower(name):
#     return True if any([ch.islower() for ch in name]) else False  #ternary operator

# if status:
#     print("There is atleast one lowercase letters")
# else:
#     print("There are no any lowercase letters")

# # any([True,False,True])-->True
# # all([[True,False,True]])---->False
# # all([True,True,True])-->True


# import string
# list_special = list(string.punctuation)
# print(list_special)

# user_input = "pokhara#$@"
# # for ch in user_input:
# #     if ch in list_special:
# #         print(f"{ch} is special character")

# mylist=[ch if ch in list_special else "" for ch in user_input]
# print(mylist)
# '''
#   gamal123--> a-True b-False c-False d-true

#  .islower() .isupper() .isdigits()
# '''

#1.take input ask from user then 
#a.contains lowercase or not
#b. contains uppercase or not
#c. contains special character or not
#d contains numbers or not


#test_data.txt--->  username,password
#--> read---> password extract ---> split
#        ----> password rank garera rank return to main function 
#main function -->  username,paswword,   strength--->    csv convert garera file(output.txt)-->write
import string

def has_lower(password):
    status = False
    for ch in password:
        if ch.islower() == True:
            status = True
    return status


def has_upper(password):
    status = False
    for ch in password:
        
        if ch.isupper() == True:
            status = True
    return status


def has_number(password):
    status = False
    for ch in password:
        if ch.isdigit() ==True:
            status = True
    return status

def has_special_character(password):
    status = False
    special_character =list(string.punctuation)
    for ch in password:
        if ch in special_character:
            status = True
    return status
            

def rank(password: str):
    if len(password) < 8 or (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)) <3:
        # rank = "POOR"
        return "POOR"
    elif len(password) <= 10 and (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)) >=3:
        # rank = "POOR"
        return "MODERATE"
    elif len(password) >10 and (has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)) == 4:
        # rank = "POOR"
        return "STRONG"


with open("passwords.txt","r") as file:
    content = file.read().split("\n")[:-1]
    print(content)

for ele in content:
    username, password = ele.split(",")
    print('-'*60)
    print(username)
    print(password)

 #1. give a function: password--> take strength of password from function
    strength = rank(password)  #strength = "POOR"
    # print(strength)

 #2. join username,password and strength (CSV)
    res = ','.join((username,password,strength))
    # print(res)

 #3.write on a file name output.txt and write csv on that file
    with open("output.txt","a") as file:
        file.write(res)
        file.write("\n")



'''
import random

funciton call
   -> lower_case = string.ascii_lowercase -->'abcdefghi----z'
   -> upper_case = string.ascii_uppercase --> 'ABCDEF...Z'
   -> numbers  = '0123456789'
   -> spcial_character ='#$%@&*()!'

   random_password = lower_case + upper_case + number +special_character --> 'abcdef...zABCDE....Z..0123456789#$%@&*()!'

   pass_length = 10

   password  = ''.join(random.sample(random_password,pass_length))

   return password
'''


#1.ask user for username--> if username exceed 20 character bhane matrai accept natra feri magni 

#2. generate a strong password for the user--> function call 
       #password = generate_password()

#3.ask the user if they want to save it or not (Y/N)
   
    #3.1 if Y 
        # username password --> join , --> yeuta file banauni suppose detail.txt
        
    #3.2 if N
        #re- generate next passowrd --> function call hunxa
         
        #3.ask the user if they want to save it or not (Y/N) 
          
           # if y 
                # username password --> join , --> yeuta file banauni suppose detail.txt
            #if N 
                #program exit kunai message print garera