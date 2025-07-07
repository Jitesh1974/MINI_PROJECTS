import random

original_num = random.randint(1,100)

guess = 0
while True:#infinite loop
 number = int(input("Enter a number from 1 to 100: "))
 guess +=1
 print('')
 if(number == original_num):
  print("Well Done You guessed it right !!!")
  print(f"The number was {original_num}")
  break# breaks loop when user guess correct number
 
 #hints to guess correct number
 elif(original_num > number):
  print("Try a greter number please !!!")

 elif(original_num < number):
  print("Try a lesser number please !!!")

#result
print('')
print(f"You guessed the number {original_num} in {guess} attempts ")
print('')
