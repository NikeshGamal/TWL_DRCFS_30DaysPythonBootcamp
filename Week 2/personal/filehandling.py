# Open the file in read-only mode
pwd = open('passwords.txt','r')
#open in read mode

print(pwd)
#file ko object lai print garxa

# Read the contents of the file
actual_file = pwd.read()

#read--> actual content haru read garxa then return to actual_file

# # Print the contents
print(actual_file)
#this prints the actual content 
pwd.close()

#to ensure that once open it should be close --> to free the memory occupied by the opened file



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------



# we use the open() function to open the file in read-only mode.
#  This means that we can read the contents of the file, 
# but we cannot modify or write to the file. 
# The open() function returns a File object, which we store in the file variable.

# After that, we use the read() method of the File object to read the contents of the file. 
# This returns a string containing the contents of the file, which we store in the contents variable.

# Next, we print the contents of the file to the console using the print() function. 
# Finally, we use the close() method of the File object to close the file. 
# This is important because it ensures that any resources used by the 
# file are properly released and available for other operations.










###########################################################

# Open the file in write-only mode
file = open("my_file.txt", "w")
#w mode ---> if note present then the file is created  if present it opens the file

# Write some text to the file

file.write("Hello, world! I am Nikesh Gamal \n")
file.write("30 Dashing Python course \n")

#write method --> use to write to the file

# Close the file
file.close()
###########################################################

# we use the open() function to open the file in write-only mode. 
# This means that we can write to the file, but we cannot read from it. 
# The open() function returns a File object, which we store in the file variable.

# After that, we use the write() method of the File object to write the string "Hello, world!" to the file.
# This overwrites any existing content in the file with the new string.

# Finally, we use the close() method of the File object to close the file.
#  This is important because it ensures that any resources used by the 
# file are properly released and available for other operations.












###########################################################
# Open the file in append mode
file = open("my_file.txt", "a")

# # Append some text to the file
file.write("\nThis is an additional line.")

# # Close the file
file.close()
###########################################################

# we use the open() function to open the file in append mode. 
# This means that we can write to the file, and the new data will be added to the 
# end of the existing content. The open() function returns a File object, which we store in the file variable.

# After that, we use the write() method of the File object to append a new line to the file. 
# This line is added to the end of the existing content in the file.

# Finally, we use the close() method of the File object to close the file. 
# This is important because it ensures that any resources used by the file are properly released and available for other operations.








# The with keyword in Python is used to open files and automatically 
# close them when they are no longer needed. This ensures that the file 
# is properly closed and any resources used by the file are released, 
# even if an error occurs during the operation.


#-----------------------------------------------------------------------------------------------

# # Open the file in read-only mode using the `with` keyword

#file inside the block will automatically will close 
with open("my_file.txt", "r") as file:
    print()
    print("------------Content inside file using with------------")
    # Read the contents of the file
    contents = file.read()

    # Print the contents
    print(contents)


#-----------------------------------------------------------------------------------------------

# we use the with keyword to open the file in read-only mode. 
# This creates a File object that is stored in the file variable. ith keyword to open the file in read-only mode. 
# This creates a File object that is stored in the file variable. The with keyword automatically closes the file when the indented code block ends.

# Inside the with block, we use the read() method of the File object to read the contents of the file. 
# Then, we print the contents to the console using the print() function.

# Using the with key
# The with keyword automatically closes the file when the indented code block ends.

# Inside the with block, we use the read() method of the File object to read the contents of the file. 
# Then, we print the contents to the console using the print() function.

# Using the with keyword is recommended when working with files in Python because 
# it ensures that the file is properly closed and any resources used by the file are released, 
# even if an error occurs during the operation. 
# This helps prevent resource leaks and other issues that can arise from improperly closing files.
