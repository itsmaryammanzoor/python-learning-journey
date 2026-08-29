# student = {
#     "Name" : "Maryam",
#     "Age" : 21,
#     "City" : "Depalpur",
#     "Marks" : 89
# }
# print(student["City"])
# student["Marks"]=90
# student["Course"]="Python"
# print(student)
# if "Email" in student:
#     print(student.get("Email"))
# else:
#     print("email does not exist!")


# # print("""Get the student's email using the get() method, 
# #           so that if Email doesn't exist, the program doesn't crash.""")

# student = {
#     "Name" : "Maryam",
#     "City" : "Depalpur",
#     "Age" : 21,
#     "Marks" : 89,
# }
# print(student.get("Email" , "Email does not exist"))
# print(student.get("Phone number", "Phone number does not exist"))
# student["Phone number"] = 3288727158
# print(student.get("Phone number"))


# #print("print the key and value together using for loop 
# #            and = sign between key and value")

# student = {
#     "name":"maryam",
#     "age": 21,
#     "city": "depalpur",
#     "course": "python",
#     "marks":89
# }
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key , value in student.items():
#     print(key ,"=" , value)


# student = {
#     "name" : "maryam",
#     "city": "depalpur",
#     "age": 29,
#     "marks":89,
# }
# if student["marks"] >=50:
#     print("you have passed")
# else:
#     print("you failed")


# print("Use a for loop to check every student's marks")

# students = {
#     "ali":67,
#     "sara":38,
#     "ahmad" :88
# }
# for key ,  value in students.items():
#     if value >= 50:
#         print(key,"=","passed")
#     else :
#      print(key,"=","failed" )



# print("check student's marks and count the pass and failed")

# students = {
#     "Ali": 75,
#     "Sara": 45,
#     "Ahmed": 88,
#     "Ayesha": 92
# }
# max = 0
# student= ""
# for key , value in students.items():
#     if value >=max:
#         max = value
#         student = key
# print("higest marks = ", max)
# print("student name is " , student)


#print("print lowest marks with student name ")
# students = {
#     "Ali": 75,
#     "Sara": 45,
#     "Ahmed": 88,
#     "Ayesha": 92
# }
# min = list(students.values())[0]
# student= ""
# for key , value in students.items():
#     if value <= min:
#         min = value
#         student = key
# print("lowest marks = ", min)
# print("student name is " , student)


#print("print hiighest marks with student name")

# students = {
#     "Ali": 75,
#     "Sara": 45,
#     "Ahmed": 88,
#     "Ayesha": 32,
#     "Hassan": 60
# }
# passed = 0
# failed = 0
# for  key , value in students.items():
#     if value >= 50:
#         passed +=1
#     else:
#         failed += 1
# print("passed = ",passed)
# print("failed = ", failed)


#print("print a list of name of passed students")
# students = {
#     "Ali": 75,
#     "Sara": 45,
#     "Ahmed": 88,
#     "Ayesha": 32,
#     "Hassan": 60
# }
# for key , value in students.items():
#     if value >= 50:
#         print(key)
    


  