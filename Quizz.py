score=0
print("Python Quizz Game ")
print("______________________________")

print("\n Question 1. what is python ?")
print("(A) normal language \n(B) programming language ")
print("(C) AI tool \n(D) search engine \n")
choice=input("Enter answer = ")
if choice == "B" or choice == "b":
    score += 2

print("\n Question 2. Operator are use for apply operation on .....")
print("(A) numbers \n(B)  language ")
print("(C) software \n(D) operands \n")
choice=input("Enter answer = ")
if choice == "D" or choice == "d":
    score += 2

print("\n Question 3. Who devloped python ?")
print("(A) James gosling \n(B) guido van rossum ")
print("(C) Dennis ritchie \n(D) charles babbage \n")
choice=input("Enter answer = ")
if choice == "B" or choice == "b":
    score += 2

print("\n Question 4. Which function is use to display output in python ?")
print("(A) input() \n(B) print() ")
print("(C) display() \n(D) show() \n")
choice=input("Enter answer = ")
if choice == "B" or choice == "b":
    score += 2

print("\n Question 5. Which Symbol is used for comments in python ?")
print("(A) // \n(B) /**/ ")
print("(C) #  \n(D) @ \n")
choice=input("Enter answer = ")
if choice == "C" or choice == "c":
    score += 2

print("\nYour answers submit successfully ")
print("Total score : 10")
print("Your score is : ",score,)