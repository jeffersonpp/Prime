import math
from datetime import datetime

bigger = 999999 # Thats the biggest number possible (approximatelly)

upper = math.floor(bigger/3) + 1 # Approximatelly the number of times iterations to reach the number 
universe = [2,3]
answer = []
print("The Strategy are:")
print("We get a List with all not multiples of 2 and 3 ")
print("math.floor(((6*(num-1)) -3 -1*(math.pow(-1,((num-1)-1))))/2)")
print("With that we iterate checking 1/3 of that numbers")


# datetime object containing current date and time
start = datetime.now()
start_string = start.strftime("%H:%M:%S")

#Delimit a Universe of not multiples of 2 and 3, what reduces the universe to 1/3 of all numbers
for num in range(2, upper + 1):
   if num > 2:
       universe.append(math.floor(((6*(num-1)) -3 -1*(math.pow(-1,((num-1)-1))))/2))
use = True
#Simple iteration between numbers to check if a number is prime
for num in universe:
        use = True
        for i in universe:
            if(i > math.floor(math.pow(num,0.5))):#analize just until reach square_root
                break
            elif(i < 4):
                continue
            elif(num % i) == 0:
                use = False
                break
        if(use):
            answer.append(num)

#print(answer)

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("START time =", start_string)
print("END time =", dt_string)
