print('WELCOME TO MY PYHTON RESTRAUNT')
print('')
menu={'pasta':80,'burger':60,'pizza':100,'salad':50,'cofee':70}
print('')
print('PLACE YOUR ORDER')

print("MENU \npasta:80\nburger:60\npizza:100\nsalad:50\ncofee:70")
print('')
n=int(input('Enter the number of items you want:'))

bill=0
for i in range(0,n):
 item=input(f"Enter the {i+1} item you want from the menu:")

 if item in menu:
  bill+=menu[item]

print(f'The total payable bill is: {bill}')
print('')
print("Thank you for visiting!!")





