# file=open("passwords.txt","r") #read only mode

# actual_content = file.read()

# print(actual_content)

# file.close()

#---------------------------------------------
#writing into file
# mini = open("mini_text.txt","w")
# #--> if present opened that particular file if not present it creates the file and then opens it

# mini.write("This is Mini's file \n")
# mini.write("This is filehandling revision class \n")


# mini.close()

#append--> existing contet kai continue ma add content

# mini = open("mini_text.txt","a")
# mini.write("This line uses write function \n")
# mini.write("THis line is to show append \n")
# mini.close()


# with ---> loop analogy

# with open("passwords.txt","r") as file:
#     print(file.read())


#--------------------String-->spilt-------------------------------

# name="NikeshGamalMiniShah"
# print(name)

# new_list=name.split("l")
# print(new_list)



#the password of ashim is pwd120

#the password of {username} is {password}
file = open("passwords.txt","r")
content =file.read()
new_list = content.split("\n") #--list

print("---------------")
print(new_list)
print("---------------")
# new_list = ["---","-----","-----"]





#1.loop each element of list
# print("Inside loop")
#2. each element lai separate or split so that we can obtain username and password

#3.print

for ele in new_list:
    username,password=ele.split(",") #--its return 2 values 
    print(f"The password of {username} is {password}")

#enumerate--> yeuta counter aafai geenerate garxa ani automatically increase garxa tyo counter ko value 
