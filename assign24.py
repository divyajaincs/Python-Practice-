courses=("Python Programming","RDBMS","Web Technology","Software Engg.")
electives=("Business intelligence","Big Data Analytics")
print(len(courses))
print(list(courses))
courses+=electives
print(courses)
courses[3]="computer Networks"
if courses[3]=="computer Networks" is True:
    print(courses)
else:
    print("tuple are immutable..")
    
    
    