import string

def has_lower(password):
    status = False
    for ch in password:
        
        if ch.islower() == True:
            status = True
    return status

def has_upper(pasword):
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

password = input('Enter the password:')

lower_case = has_lower(password)
upper_case = has_upper(password)
digits = has_number(password)
speical_character = has_special_character(password)

#1.check for the condition
"""
password-->
a.length of characters less than 8 -->POOR 
  or satisfy less than 3 condition --> POOR

b.length of character 8-10 
 and satisfy 3 or more condition -->MODERATE

 c. length of character more than 10
    satisfy all conditions --> STRONG
"""

# has_lower(password)+has_upper(password)+has_number(password)+has_special_character(password)

#True+False+True+False= 2

if len(password) <8 or (lower_case+upper_case+digits+speical_character)<3:
    rank="POOR"
    # print(f"The rank of the password is {rank}")
elif len(password)<=10 and (lower_case+upper_case+digits+speical_character)>=3:
    rank="MODERATE"
    print(f"The rank of the password is {rank}")
elif len(password)>10 and (lower_case+upper_case+digits+speical_character)==4:
    rank="STRONG"
    print(f"The rank of the password is {rank}")


#file username,password 
# 1.read split--> username and password --> password chai function ma pass garni then determine garni POOR, MODERATE or STRONG
# 2.arko file banauni --> file.write--> username,password,rank

'''
'''