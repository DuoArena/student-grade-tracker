import numbers


print("Student tracker starting...")
numstudents= int(input("How many students do you have?: "))
numsubjects =int(input("How many subjects do they study?"))

names = ["" for _ in range(numstudents)]
grades = [[0 for _ in range(numsubjects)]
          for _ in range(numstudents)]
# initializing names list and grades 2d arrays
finalgrade = ["" for _ in range(numstudents)]
#initializing separate array for final grade


for studentcount in range(numstudents):
    total= 0
    name = str(input("Enter Student name:"))
    for subjectcount in range(numsubjects):
        print("Enter marks for subject",subjectcount,":")
        studentgrade = int(input())
        grades[studentcount][subjectcount] = studentgrade 
        total += studentgrade      
    averagegrade = int(round((total / numsubjects),0))
    #made average grade calculator 
    names[studentcount] = name
    grades[studentcount].append(averagegrade)
    if averagegrade >= 80:
        print("This student has then EXCELLENT")
        finalgrade[studentcount] = str("EXCELLENT")
    elif averagegrade < 80 and averagegrade >= 60:
        print("This student has done PASSING")
        finalgrade[studentcount] = str("PASSING")
    else:
        print("This student has underperformed, requires more help")
        finalgrade[studentcount] =  str("UNDERPERFORMING")
    #Implement grade assignment based on average

#Start displaying their grades and Such

print("=====================================")
print("Student Report")
print("=====================================")

for i in range(numstudents):
    marks = grades[i][:-1]
    avg = grades[i][-1]
    #Stores all the values in the grade array except for the last and avg stores only the last thing in the array(aka average)

    print(names[i])
    print("Marks:", marks)
    print("Average:", avg)
    print("Result:", finalgrade[i])
    print("----------------------------------")





    





        

