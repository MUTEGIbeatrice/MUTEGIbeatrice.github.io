  As from my Individual Essay, not only did it mention the benefits of the web-based Appointment and Scheduling Management Information System (ASMIS) to Queens Medical Centre and the sick residents, but also highlighted the potential cyberthreats, and know-how design and implementation of a secure system. 
  
  Below is a description of a few Python code solutions that can be applied in the Appointment and Scheduling Management Information System (ASMIS) to ensure reinforcement of Cybersecurity. These codes include:
  
  **1).	Custom Password Validating Code:**
  - In order to ensure that a user has a strong password, a code can be used to validate the password. 
  - In the code, Regular Expressions (RegEx or re) is imported so that ‘re.search()’ method can be used to search and detect a pattern of strings within a given criteria (Lenka, 2020). 
  - First, it prompts for a password input.
  - Then checks the inputted password so as to confirm if all the below parameters are met:
          o	Is between 8 and 20 characters long - ‘or’ Boolean operator was used to join the code arguments into one statement (Novak, 2019)
          o	Has at least 1 capital letter 
          o	Has at least 1 small letter
          o	Has any of these symbols, which are ~ ! @ # $ % ^ & 
          o	Has at least 1 digit number
          o	Has no space
  - If any of the above criteria are not met, the system outputs an error message.
  - While loop is included in the code so as to allow repetition of the password_validator() function and ‘break’ is used to stop prompting the user for a password input when all the above criteria are met and validated (Campbell, 2022). 

  **2).	One-Time Pin/Password (OTP) Generating Code:** 
  - This code provides the user with an output of a One Time Pin or Password (OTP) that has 6 digits (by assigning a variable that has numbers and both capital and small letters and using for loop to define the 6-digit length of the OTP) (Anon, N.D.). 
  - Importation of random library allows generation of any random numbers while math library gives access to common mathematical functions (Oliphant, 2007).
  - This 6-digit code can then be used by the user to authenticate the second or third time so as to be granted access to his/her account.

  **3).	Custom Password Generator Code:** 
  - Since most users do not want to spend time thinking of new passwords every time they sign up to a new account or change passwords, password generating feature can be useful in eradicating password repetitions across a user’s accounts. 
  - This code, generate_password() function, has imported the random library and assigned a variable (string) and datatype (str) to all the characters that are to be included in the new password.
  - It first asks the user to input the length of the password he/she intends to generate. 
  - If statement and ‘or’ Boolean operator checks if the length of the password inputted is between 8 to 20 and if it is not, it displays an error message.
  - While loop allows repetition of the user’s input until a correct number is entered. 
  - After a true pass, the Random sample() method and join() method joins the random data as per the length and criteria entered, thus generating and outputting the password (Rawat, 2020).

  **4).	Time-Based Login of 3 Attempts and Login Blocking Code:** 
  - This code helps in fighting cyberattacks like brute force, etc.
  - This code gives the user 3 attempts of inputting his/her username and password (which are already registered in the system as: **Username: Student1 and Password: Password1**).
  - After a failed attempt, the code gives you 5 seconds before inputting your credentials again and if the number of failed attempts is exhausted to 3, the program will block the login (Wind & , 2021). 
  - This is made possible by importing the time library, and usage of nested if condition and while loop.


**References**
Anon, N.D.. Write a Python program to generate a One Time Password OTP. [Online] 
Available at: https://codedec.com/tutorials/write-a-python-program-to-generate-a-one-time-password-otp/
[Accessed 28 May 2022].

Campbell, S., 2022. Python Loops While For Break, Continue Enumerate. [Online] 
Available at: https://www.guru99.com/python-loops-while-for-break-continue-enumerate.html
[Accessed 29 May 2022].

Lenka, C., 2020. Python program check validity Password. [Online] 
Available at: https://www.geeksforgeeks.org/python-program-check-validity-password/
[Accessed 28 May 2022].

Novak, N., 2019. Python if statements. [Online] 
Available at: https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=1036&context=bx_oers
[Accessed 29 May 2022].

Oliphant, T. E., 2007. Python for Scientific Computing. Computing in Science and Engineering, 9(3), pp. 10-20.

Rawat, A., 2020. Create a Random Password Generator using Python. [Online] 
Available at: https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
[Accessed 29 May 2022].

Wind, A. & R., 2021. Block login if too many login attempts. [Online] 
Available at: https://stackoverflow.com/questions/69892361/block-login-if-too-many-login-attempts
[Accessed 29 May 2022].




