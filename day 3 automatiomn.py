# marks=int(input("Enter your marks: "))
# if marks>=50:
#  print("Congratulations! you passed.")
# else: 
#  print("Sorry! you failed.")

# age=int(input("Enter your age: "))
# if age>=18:
#  print("You are eligible to vote.")
# else: 
#  print("You are not eligible to vote.")

# marks=int(input("Enter your marks"))
# if marks>=90:
#     print("your grade is A+")
# elif  marks>=80:
#     print("your grade is A")
# elif marks>=70:
#     print("your grade is B")
# elif marks>=60:
#     print ("your grade is C")
# elif marks>=50:
#     print("your grade is D")
# else:
#     print("you failed!")


# UN = "admin"
# PC = 1234
# username = input("enter username: ")
# password = int(input("enter password:  "))
# if username == UN and password == PC:
#    print ("Login Successful!")
# else:
#    print ("Invalid Username or Password!")


# UN = "admin"
# PC = 1234
# username = input("enter username: ")
# password = int(input("enter password:  "))
# if username == UN and password == PC:
#     print("Login Successful!")
# elif username != UN:
#     print("Invalid Username!")
# elif password != PC:
#     print("Incorrect Password!")
# else:
#     print ("Invalid Username or Password!")





print("1. Check Balance ")
print("2. Deposit")    
print("3. Withdraw")
choice=int(input("Choose one: "))
if choice == 1:
    print("Your balance is Rs.5000.")
elif choice == 2:
    print("Deposit Successful!")
elif choice == 3:
    print("Withdrawl Successful!")
else:
    print("Invalid Choice!")