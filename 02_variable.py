1) WHAT  is variable ?
. A variable is a name that stores data in your program. Think of it as a container for values
___________________________________________________________________________________________________________________________________________________________________________________________________________2) 
2) RULES TO WRITE VARIABLE?
.variable name can't start with anumber
. use letter ,number ,and underscore
.variable names are case senstive 
__________________________________________________________________________________________________________________________________________________________________________________________________________
EXAMPLE:
name = "prashanti"
age=20
____________________________________________________________________________________________________________________________________________________________________________________________________________
3) WHERE DO I USE VARIABLE ?
.inside the function(local variable)
.outside the function(golbal variable)
.inside the lOOP
-> INSIDE THE FUNCTION(local variable)
 . use it when the value is only needed inside that function
   def greet():
     message= "hello"
     print(message)
  greet():

-> OUTSIDE THE FUNCTION(golbal variable)
.use it when multiple functions need to access the same value
   name ="prashanti"
def greet():
  print("hello",name)
greet():
print(name)

-> LOOP VARIABLE
. use it for that change repeatedly
   for i in range(3):
     temp=i*2
     print(temp)
_______________________________________________________________________________________________________________________________________________________________________________________________________________
 SWAP 2 NUMBER 
   a=input("enter value of a=")
   b=input("enter the value of b=")
   temp=a
   a=b
   b=temo                                 (... INPUT= it uses when we want take inputs fron user)
   print("a="+a)
   print("b="+b)
_____________________________________________________________________________________________________________________________________________________________________________________________________________
THERE ARE THREE TYPES CASES  TO WRITE VARIBALE 
  .camel case
  .pascal case
  .snake case

  ->CAMEL CASE:
myName(m should be in samll and N should in capital)
myVariableName( m should in small  V  and N should be captal)

  -> PASCAL CASE:
  MyName( M and N should be capital)
  MyVariableName(M ,V,N should be capital)

  -> SNAKE CASE:
   my_variable_name
  _________________________________________________________________________________________________________________________________________________________________________________________________________________
   HOW TO ASGIN VARIABLE
-> Assgin a number
   a=10
   b=20
-> assign text(String)
 name="alice"
-> assign value from user input
age=input("enter your age:")
->assign mutliple variable at once
  x,y=5,10

    
  

  
  

           
    





  

















/
  
                                                                                 
