def add(x,y):
 pass
 
#Subtract implemetation
def subtract(x,y):
 return x-y             #on master branch

#Multiply implemetation
def multiply(x,y):              #on bug456 branch
 return x*y

#Divide implemetation
def divide(x,y):             #on master branch
 if y==0 :
       return DIVIDE_BY_ZERO_ERROR
 else :
       return x/y 

#square implementation
def square(x):
   return x*x