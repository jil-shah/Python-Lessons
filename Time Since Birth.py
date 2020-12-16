##Jil Shah
##596358
##ISC-3UO-D
##Number of days and sleep hours
##Feb 20 2018
##Mr Veera
print ("Enter your birthday:")

year1= int(input("Year:"))
month1=int(input("Month:"))
day1=int(input("Day:"))

print("Enter todays date")

year2= int(input("Year:"))
month2=int(input("Month:"))
day2=int(input("Day:"))

yearinterval= year2-year1
monthinterval= month2- month1
daysinterval= day2-day1

year_days=365*yearinterval
month_days= 30*monthinterval


Total_days= year_days+month_days+daysinterval
print("You have been alive for",Total_days)
sleep_hours= 8*Total_days
print ("You have slept for",sleep_hours)
