# def sum_of_numbers(num1,num2):
#     print("Inside function")
#     sum= num1+num2
#     # print(sum)
#     print("Inside function")
#     return sum
# #calculation 
#     # return 

# """
#   o/p--> function bhitraii print --->print()
#   0/p --> main function ma print garni ho 
# """
# print("Outside function")
# print(sum_of_numbers(3,4))
# # print(result)#sum
# print("Outside function")


#1.username password input 
#2.functino ma pass --> username password
    #3.csv--> comma separated vlaues username,password
    #4,. string --> username,password
#5. varaible -->print

def csv_file(username,password):
    print("inside function")
    # print(username,password)
    res = ','.join((username,password))
    # print(res)
    return res


username=input("Enter username: ")
password = input("Enter password: ")

# csv_variable=csv_file(username,password)
# with open()as file
# file.wri(vs)