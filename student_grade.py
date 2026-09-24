import pandas as pd
data={"name":[],"marks":[],"grade":[]}
num=int(input("Enter no. of student : "))
for i in range(1,num+1):
    print("\n Enter detail of student no.",i)
    data["name"].append(input("Enter name of student : "))
    data["marks"].append(int(input("Enter marks of student : ")))
for i in data["marks"]:
    if i>=60 and i<=100:
        data["grade"].append("First")
    elif i>=45:
        data["grade"].append("Second")
    elif i>=33:
        data["grade"].append("Third")
    else:
        data["grade"].append("Fail")
df=pd.DataFrame(data)
print(df.sort_values(by="name" ,ascending=True))