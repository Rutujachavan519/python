# working of break statement for loop
for i in range(1,6):
  if i==4:
    break
print(i)
print("Loop Ended")

# working of break statement while loop
count=1
while count<=5:
  if count==3:
    break
  print(count)
count +=1
print("Loop Terminated")