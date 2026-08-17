# develope a program that a student mark for 3 different subject calculate the total , avg and print final score card with the avg rounde in 2 decimal
print("============================ Final Score Card ==============================")
name=input("Enter a Name :")
roll=int(input("Enter a Roll no:"))
subject1=int(input("Enter a Subject 1 marks :"))
subject2=int(input("Enter a Subject 2 marks :"))
subject3=int(input("Enter a Subject 3 marks :"))

total=subject1+subject2+subject3
avg=total*100/300

print("--------------------------- Final Score Card-----------------------")
print("Name :",name)
print("Roll No :",roll)
print("Subject 1:",subject1)
print("Subject 2:",subject2)
print("Subject 3:",subject3)
print("Total:",total)
print("percentage:",avg)

