marks=[]
num_students= int(input("number of students:"))
marks_stud =int(input ("number of marks per student"))

final_marks=[]
def final ():
    counter=0
    while counter!= num_students:
        for i in range (0,marks_stud):
            final_marks.append(marks[0])
            del (marks[i])

        print (final_marks )
    counter+=1
    
for i in range (num_students*marks_stud):
    mark= int (input ("mark:"))
    marks.append(mark)
final()
