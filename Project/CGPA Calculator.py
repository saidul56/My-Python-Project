sum1=0
sum2=0
print("Input total course number in your semester :")
n=int(input())

for x in range(n):
    print("Enter your course credit and CGPA")
    c=float(input("Credit : "))
    cg=float(input("CGPA : "))
    y=c*cg
    sum1+=c
    sum2+=y
    z=sum2/sum1
print("Your CGPA is : ",z)    