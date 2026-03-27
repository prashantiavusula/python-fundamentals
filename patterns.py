"""
#right angle triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
"""
"""
#inverted right angle triangle pattern
n=5
for i in range(1,n+1):
    for j in range(5,i-1,-1):
        print("*",end="")
    print()
"""
"""
pyramid
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i):
        print("*",end="")
    print()
"""
"""
#inverted pyramid triangle
n=5
for i in range(5,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
#daimond pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""

"""
#hoolow square
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#full square
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
"""
"""
##inverted triangle(number pattern)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""
"""
#inverted triangle
n=5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""

"""
#floyd;s pattern
n=int(input("enter the number:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
"""
"""
#hollow right angle
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  i==n or j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#hollow pyramid
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if  k==2*i-2 or k==0 or  i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#hollow pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 or i==n:
            print("*",end="")
        else:
            print(" " ,end="")
    print()
"""
"""
#hollow daimond pattern(number pattern)
n=5 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print(i,end="")
        else:
            print(" ",end="")
    print()
for i in range(5,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print(i,end="")
        else:
            print(" ",end="")
    print()
"""

"""
#15.butterfly pattern 
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end="")
    for j in range(2*(n-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
"""
"""
#hallow pyramid pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print(i,end="")
        else:
            print(" ",end="")
    print()
"""
"""
#full star pyramid
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
#inverted full star pyramid
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
#left alligned triangle 
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
"""
"""
#right alligned trinagle
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
"""
"""
#hourglass pattern
n=5 
for i in range(5,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
#diamond shape with number
n=5 
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print(i,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print(i,end="")
    print()
"""
"""
#hollow rhombus pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#numeric pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""
"""
#hollow diamond with number
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print(i,end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print(i,end="")
        else:
            print(" ",end="")
    print()
"""
"""
#reverse ptramid pattern with number
n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(k,end="")
    print()
"""
"""
#daimond star pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
"""
"""
#full number pattern
n=5
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()
"""
"""
#check board pattern
n=5
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#rhomus pattern for numbers
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in  range(2*i-1):
        print(k+1,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print(k+1,end="")
    print()
"""
"""
#hollow inverted pyramid
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#crosspattern
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""
"""
#parallogram pattern
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")
    print()
"""
"""
#rectangle with number
n=5
for i in range(1,n+1):
    for j in range(n):
        print(j+1,end="")
    print()
"""
            

        




    




               



