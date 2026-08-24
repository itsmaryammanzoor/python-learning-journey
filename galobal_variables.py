# global variables
# when you want to use value of x given inside the function
x="fun"
def myFun():
    x="fantastic"
    print("python is ",x)  
myFun()

print("---------------------") 

# when you want to use value of x given outside the function
x="fun"
def myFun():
    x="fantastic" 
myFun()
print("python is ",x) 

print("---------------------") 

# *global keyword*
# # use of x as global every where while it is created inside the function
x="fun"
def myFun():
    global x
    x="fantastic" 
    print("python is ",x) 
myFun()
print("python is ",x) 
