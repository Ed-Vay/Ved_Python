val=float (input("Enter 1st number here-"))
val2=float (input ("Enter 2nd number here-"))
operation = input ("Enter operation You want to perform, Eg.+,-,*,/ here- ")
if operation == "+":
   result= (val)+(val2)
elif operation == "-":
   result= (val)-(val2)
elif operation == "*":
   result= (val)*(val2)
elif operation == "/":
   result= (val)/(val2)
else :
    print("invalid operation")
print ("The answer is=",float (result))
