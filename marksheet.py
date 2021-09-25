
# python program to print the student mark sheet

subjects = ["Chemistry", "C Programming", "Mathematics",
            "Environment", "Electrical & Electronics", "Machine Engineering"]
subjcode = ["CH-102", "CS-102", "MA-111", "CS-107", "EE-101", "ME-101"]
midmarks = []
semmarks = []
count = MTotal = 0

name = input("Enter Your Name:")
fname = input("Enter Your Father Name:")
rnumber = input("Enter Your Roll Number:")
college = input("Enter Your College Name:")

for x in subjects:
    a = int(input("Enter midterm marks for"+x))
    b = int(input("Enter semester marks for"+x))
    midmarks.append(a)
    semmarks.append(b)

print("\n\n\t\t******************************* Your RESULT *****************************************\n\n")

print("\t\tCOLLEGE: ",college)
print("\n\t\tNAME: ",name,"\t\tFATHER NAME: ",fname)
print("\n\t\tROLL NUMBER: ",rnumber)

print("\n\t\t SUBJECTS              MARK1             MARK2           TOTAL")

for (x,y,z) in zip(subjcode,midmarks,semmarks):
    print("\n\t\t",x, "              ",y,"            ",z,"           ",y+z)
    MTotal = MTotal +y+z
    if y+z < 44:
        count +=1

if count == 0:
    print("\n\t\tTOTAL MARKS:",MTotal,"\t\tRESULT: PASS")
else:
    print("\n\t\tTOTAL MARKS:",MTotal,"\t\tRESULT: FAIL")
