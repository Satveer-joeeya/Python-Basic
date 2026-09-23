import pandas as pd
data={"name":[],"marks":[]}
num=int(input("Enter no. of student : "))
for i in range(1,num+1):
    print("\n Enter detail of student no.",i)
    data["name"].append(input("Enter name of student : "))
    data["marks"].append(int(input("Enter marks of student : ")))