number = int(input("Please input a number:"))
if number%2 == 0:
    print("this is even")
else :
    print("this is odd")
last = input("Please input your student ID first character:")
studentID = int(input("Please input your student ID last 8 number:"))
if studentID%2 == 0:
    print("your student ID number is even")
else:
    print("your student ID number is odd")
print("your student ID is :"+last+str(studentID))