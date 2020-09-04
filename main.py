# Author: Chang Li cxl5844@psu.edu

G1 = input("Enter your course 1 letter grade: ")
C1 = input("Enter your course 1 credit: ")
if G1 == 'A' : 
  P1 = 4.0
  print("Grade point for course 1 is: 4.0")
elif G1 =="A-" : 
  P1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif G1 =="B+" : 
  P1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif G1 =="B" : 
  P1 = 	3.0
  print("Grade point for course 1 is: 3.0")
elif G1 =="B-" : 
  P1 = 	2.67
  print("Grade point for course 1 is: 2.67")
elif G1 =="C+" : 
  P1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif G1 =="C" : 
  P1 = 	2.0
  print("Grade point for course 1 is: 2.0")
elif G1 =="D" : 
  P1 = 	1.0
  print("Grade point for course 1 is: 1.0")
else: 
  P1 = 	0.0
  print("Grade point for course 1 is: 0.0")

G2 = input("Enter your course 2 letter grade: ")
C2 = input("Enter your course 2 credit: ")
if G2 == 'A' : 
  P2 = 4.0
  print("Grade point for course 2 is: 4.0")
elif G2 =="A-" : 
  P2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif G2 =="B+" : 
  P2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif G2 =="B" : 
  P2 = 	3.0
  print("Grade point for course 2 is: 3.0")
elif G1 =="B-" : 
  P2 = 	2.67
  print("Grade point for course 2 is: 2.67")
elif G2 =="C+" : 
  P2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif G2 =="C" : 
  P2 = 	2.0
  print("Grade point for course 2 is: 2.0")
elif G2 =="D" : 
  P2 = 	1.0
  print("Grade point for course 2 is: 1.0")
else: 
  P2 = 	0.0
  print("Grade point for course 2 is: 0.0")

G3 = input("Enter your course 3 letter grade: ")
C3 = input("Enter your course 3 credit: ")
if G3 == 'A' : 
  P3 = 4.0
  print("Grade point for course 3 is: 4.0")
elif G3 =="A-" : 
  P3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif G3 =="B+" : 
  P3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif G3 =="B" : 
  P3 = 	3.0
  print("Grade point for course 3 is: 3.0")
elif G3 =="B-" : 
  P3 = 	2.67
  print("Grade point for course 3 is: 2.67")
elif G3 =="C+" : 
  P3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif G3 =="C" : 
  P3 = 	2.0
  print("Grade point for course 3 is: 2.0")
elif G3 =="D" : 
  P3 = 	1.0
  print("Grade point for course 3 is: 1.0")
else: 
  P3 = 	0.0
  print("Grade point for course 3 is: 0.0")

c1=float(C1)
c2=float(C2)
c3=float(C3)

GPA=0.0
GPA += P1*c1+P2*c2+P3*c3
print(GPA)
GPA /=(c1+c2+c3)

print("Your GPA is: " + str(GPA))