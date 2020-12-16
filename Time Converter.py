##Jil Shah
##596358
##ISC-3UO-D
##Time Converter
##May 7th 2018
##Mr Veera

def hours_to_minutes():
    new_time= time*60
    print(new_time)
def minutes_to_hours():
    new_time= time/60
    print(new_time)
def days_to_hours():
    new_time= time*24
    print(new_time)
def hours_to_days():
    new_time= time/24
    print(new_time)

time_unit=input("")
time=int(input())
time_end_unit=input("")

if time_unit=="hours" and time_end_unit=="minutes":
    hours_to_minutes()
elif time_unit=="minutes" and time_end_unit=="hours":
    minutes_to_hours()
elif time_unit=="days" and time_end_unit=="hours":
    days_to_hours ()
elif time_unit=="hours" and time_end_unit=="days":
    hours_to_days ()
