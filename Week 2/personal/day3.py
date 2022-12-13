#password.txt to ko password lai list ma  store garni 

username_pwd= open("passwords.txt",'r').read()
details_list = username_pwd.split("\n")
print('The data inside file is ')
print(username_pwd)
print()
user_details={} #defining dictionary
# print(username_pwd)
for ind,ele in enumerate(details_list):
    username,password =ele.split(',')

    print(f"The password of {username} is {password}")

    #adding element to dictionary
    user_details[username]=password
    # print(ind,ele)

print('-'*60)
print(user_details)