# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 
import re

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
    regex_characters= "[^a-zA-Z0-9]+"
    special_character = re.compile(regex_characters)
    search_character = re.search(special_character,pwd)

    regex_lower="[a-z]+"
    lowercase_string = re.compile(regex_lower)
    search_lower = re.search(lowercase_string,pwd)


    regex_capital="[A-Z]+"
    uppercase_string = re.compile(regex_capital)
    search_capital = re.search(uppercase_string,pwd)
    

    regex_numbers = "[0-9]+"
    number_string = re.compile(regex_numbers)
    search_number = re.search(lowercase_string,pwd)

    rank="NOT DEFINED"
    if len(pwd)<8 or False:
        rank="POOR"
    elif len(pwd)<= 10 or False:
        rank="MODERATE"
    elif search_capital and search_character and search_lower and search_number:
        rank="STRONG"
        # print(type(re.search(special_character,pwd)))

    ## End code here
    return rank

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE

    ## END CODE HERE

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def random_password_generator():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''
    sp_ch_list=list(string.punctuation)
    special_character=sp_ch_list[random.randint(0,len(sp_ch_list)-1)] +sp_ch_list[random.randint(0,len(sp_ch_list)-1)]+sp_ch_list[random.randint(0,len(sp_ch_list)-1)] +sp_ch_list[random.randint(0,len(sp_ch_list)-1)]

    # print(special_character)
    lower_list=string.ascii_lowercase

    lower_case=lower_list[random.randint(0,len(lower_list)-1)] +lower_list[random.randint(0,len(lower_list)-1)]+lower_list[random.randint(0,len(lower_list)-1)]
    # print(lower_case)

    upper_list=string.ascii_uppercase
    upper_case=upper_list[random.randint(0,len(upper_list)-1)] +upper_list[random.randint(0,len(upper_list)-1)]+upper_list[random.randint(0,len(upper_list)-1)]

    # print(upper_case)
    numbers=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    # print(numbers)

    password_list=[lower_case,upper_case,special_character,numbers]
    # print(password_list)
    # print("*"*100)
    random.shuffle(password_list)

    generated_password=""

    for ele in password_list:
        generated_password+=ele
    
    return generated_password

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE

        ## END CODE HERE
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE

    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE

    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
        option = int(inp)
        # print(type(option))
        if option == 1:
            with open("Users-Pwds(10).txt","r") as file:
                contents = file.read()[:-1].split("\n")
                # print(contents)
            for ele in contents:
                # print(ele)
                details=ele.split(",")
                username,password = details
                # print(username,password)
            #function to detemine the password strength
                strength=rank(password)
                # print(strength)
                # output_result = ','.join((username,password,strength))
                # print(output_result)
                with open("Users-Pwds-Chked.txt",'a') as output:
                    output.write(','.join((username,password,strength)))
                    output.write("\n")
            print("Rank Password from an existing file Successfull")
        elif option == 2:
            while True:
                username=input("Enter desirable username not more than 20 characters: ")
                if len(username)<=20:
                    break
            print(username)

            password = random_password_generator()
            print(f"Username: {username}")
            print(f"Newly Generated Password: {password}")

            
            ans=input("Would you like to save the password? (Y or N)").upper()

            if ans =="Y":
                with open("Users-Pwds.txt","a") as file:
                    file.write(','.join((username,password)))
                    print("Password saved successfully")
            else:
                ans=input("Would you like to generate another password? (Y or N)").upper()
                if ans=="Y":
                    new_generated_password=random_password_generator()
                    password-new_generated_password
                else:
                    print("Previously generated password is saved as password")
                    with open("Users-Pwds.txt","a") as file:
                        file.write("\n")
                        file.writelines(','.join((username,password)))
                        # TODO: line is not breaking
        elif option ==3:
            print("End of program")
            break
        else:
            print("ENTER THE CORRECT OPTION FROM THE GIVEN OPTIONS")
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()