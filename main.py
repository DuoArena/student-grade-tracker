print("Student tracker starting...")
numstudents= int(input("How many students do you have?: "))
numsubjects =int(input("How many subjects do they study?"))

names = ["" for _ in range(numstudents)]
grades =  [[0 for _ in range(numstudents)] for _ in range(numsubjects)]
# initializing names list and grades 2d arrays

for studentcount in range(numstudents):
    total= 0
    name = str(input("Enter Student name:"))
    for subjectcount in range(numsubjects):
        print("Enter marks for subject",subjectcount,":")
        studentgrade = int(input())
        grades[studentcount][subjectcount] = studentgrade 
        total = total + studentgrade      
    averagegrade = float(round((total / numsubjects),0))
    #made average grade

        

