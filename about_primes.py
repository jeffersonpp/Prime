import math

bigger = 999999 # Thats the biggest number possible (approximatelly)

upper = math.floor(bigger/3)+2 # Approximatelly the number of times iterations to reach the number 
universe = [2,3]
print("The Strategy are:")
print("We get a List with all not multiples of 2 and 3 ")
print("math.floor(((6*(num-1)) -3 -1*(math.pow(-1,((num-1)-1))))/2)")
print("With that we iterate checking 1/3 of that numbers")

#Delimit a Universe of not multiples of 2 and 3, what reduces the universe to 1/3 of all numbers
for num in range(2, upper + 1):
   if num > 2:
       universe.append(math.floor(((6*(num-1)) -3 -1*(math.pow(-1,((num-1)-1))))/2))

#Simple iteration between numbers to check if a number is prime
for num in universe:
       for i in range(2, math.floor(math.pow(num,0.5))):
           if (num % i) == 0:
               break
       else:
           print(num)