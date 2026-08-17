marks=float(input("Enter graduation score :"))
backlogs=int(input("Enter number of active backlogs:"))

if marks>70:
    if backlogs==0:
        print("Eligible for placement ")
    else:
        print("Not Eligible : Active bacloga are present")
else:
    print("Not Eligible : Graduation score is below 70% 800") 