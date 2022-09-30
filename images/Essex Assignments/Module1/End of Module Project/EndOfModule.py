#Custom Password Validator 
#https://www.geeksforgeeks.org/python-program-check-validity-password/

print("End of Module Assignment")


def password_validator():#defining a function

  """passwordvalidator"""

  import re #importing regex (re) library

  print("Password Validator")

  while (True): #allows looping till all have a positive check

    password= str(input("Please Enter Password: "))#assigns a variable and data type to user's input and also prints out a message asking the user for an input

    if (len(password)<8 or len(password)>20): #used or boolean operator to check the character length
      print('Password should be between 8 and 20 characters long ')

    elif not re.search("[A-Z]", password): #the searching regex checks the input and if it does not have a capital letter, the message below will be printed
      print('Password should have atleast 1 capital letter') 

    elif not re.search("[a-z]", password): #the searching regex checks the input and if it does not have a small letter, the message  below will be printed 
      print('Password should have atleast 1 small letter')

    elif not re.search("[1-9]",password): #the searching regex checks the input and if it does not have a number, the  message below will be printed 
      print("Password should have atleast one number between 1 to 9")

    elif not re.search("[~!@#$%^&*]",password): #the searching regex checks the input and if it does not have a symbol, the  message below will be printed 
      print("Password should have at least one of these symbols ~ ! @ # $ % ^ & * ")

    elif re.search(" ",password): #the searching regex checks the input and if it has a space, the message below will be printed 
      print("Password should not contain any space")

    else: #if the input passes all the checks, it will output password is valid
      print("Password is valid")

      break  # it stops the loop once it outputs that the password is valid
 
password_validator() #closing the function





#Generating and Printing a One Time Password/Pin (OTP) of 6 digit length
#https://codedec.com/tutorials/write-a-python-program-to-generate-a-one-time-password-otp/ 

def generate_OTP(): #defined the function

  import math, random # imported math and random libraries

  string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #defines all the characters that will be included in the generated OTP as a string data type 

  OTP = "" #assigns a variable

  print('One Time Password/Pin (OTP) Generator') #outputs this as a title

  length = len(string) #assigns a variable 

  for i in range(6): #defing the length of the OTP using for loop
      OTP += string[math.floor(random.random() * length)] #using the math and random library to generate a 6 digit OTP
  return OTP #returns the 6 digit OTP 

if __name__ == "__main__":
  print("6 length OTP is:", generate_OTP()) #outputs the 6 digit OTP





#Custom Password Generator
#https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9

def generate_password(): #defining the function
  import random #importing random library

  string = str('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*')

  password = ""#assigns a variable

  print ("Password Generator") #outputs this as a title

  while (True): #enables looping of code until it reaches a true statement

    length = int(input("Enter the length of password: ")) #assigns a variable and data type to user's input and also prints out a message asking the user for an input

    if ((length < 8) or (length>20)): #used or boolean operator to check that the input entered is between 8 and 20, and if it is not it will output the message below
      print('Password length should be between 8 to 20 characters long')
        
    else:
      password="".join(random.sample(string,length))#Assigns a variable and joins the random data as per th length entered 
      return password
         
print("Your Password is: ", generate_password()) #outputs the generated password




#5 second Time-based login of 3 Attempts and after it is blocked
#https://stackoverflow.com/questions/69892361/block-login-if-too-many-login-attempts

def login_attempt(): #defining the function
  
  import time #importing time library 

  print("Time-based Login Attempt")

  print('Enter the Correct Username and Password to Continue') #outputting an instruction to the user

  max_attempts=int(3) #assigning a variable and data type to show the number of times/attempts it will accept to run

  attempts=int(0) #assigning a variable and data type

  while True: #use while loop to repeat the code of input and validation of credentials

    username = str(input("Enter the Username: "))  #prompting for an input from the user and Assigning a variable and datatype on the inputted data
    password = str(input("Enter the Password: ")) #prompting for an input from the user and Assigning a variable and datatype on the inputted data

    if password=='Password1' and username=='Student1':#using if statement to set a condition
      print('Access Granted')
      break

    else: 
      attempts+=1
      if attempts>= max_attempts: #setting a condition of what will be outputted after 3 failed attempts are up
        print("Access Blocked After 3 Attempts. Please Restart the Program and Try Again.")
        break

      print("Access Denied. Try again in 5 seconds.") #the output will be shown after a failed input during the 3 attempts
     
    time.sleep(5) #the time in seconds set to wait before the user tries to input the credentials again
    
               
login_attempt()   #closing the function


#Exiting 
print('Thank You and Goodbye')
exit=str(input("Press Any Key to Exit: "))
print('Thank You and Goodbye')


  