import math
principle=eval(input("intial principle"))
interest= eval(input("interest"))
compound=eval(input("number of times compounded per year"))
time= eval(input("time"))

## part a
A1= principle*((1+(interest/compound))**(compound*time))
print (A1)

##part b
A2= principle
for i in range (1,(compound*time)+1):
    A2= A2*(1+interest/compound)
print (A2)

##part C
B= principle*(math.exp(interest*time))
print (B)

##part D
RD1= 100*abs((A1-A2)/A1)
print(RD1)

##part E
RD2=100*abs((A1-B)/B)
print(RD2)
