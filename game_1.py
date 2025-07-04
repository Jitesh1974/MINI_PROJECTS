import random

print("LET'S PLAY ROCK PAPER SCISSOR !!!!!!")
print('')
def game( your_score,comp_score): 
  
 computer_choice=random.randint(1,3)

 your_choice=input("ENTER ROCK(R)/PAPER(P)/SCISSOR(S) : ")

 your_dict={'R':1,'P':2,'S':3,'r':1,'p':2,'s':3}

#checking the valid input 
 if your_choice not in your_dict:
    print("INVALID INPUT! ROUND SKIPPED.")
    return your_score, comp_score

 you=your_dict[your_choice]
  
#printing your choice
 if(you==1):
  print("YOU CHOOSED: ROCK")
 elif(you==2):
  print("YOU CHOOSED: PAPER")
 else:
  print("YOU CHOOSED: SCISSOR")

#printing computer choice
 if(computer_choice==1):
  print("COMPUTER CHOOSED: ROCK")
 elif(computer_choice==2):
   print("COMPUTER CHOOSED: PAPER")
 else: print("COMPUTER CHOOSED: SCISSOR") 

#main game logic
 if(computer_choice==you):
     print('DRAW')      
 else:
    if((computer_choice==1 and you==2) or (computer_choice==2 and you==3) or\
       (computer_choice==3 and you==1)):
       print('YOU WON')
       your_score+=1
    else:
       print('YOU LOST')
       comp_score+=1
 return your_score,comp_score#end of game fn

#main prog starts      
rounds=int(input('ENTER THE NUMBER OF ROUNDS: '))
your_score=0#score at starting of match
comp_score=0 

for i in range(1,rounds+1):
  print('')
  print(f'ROUND {i}')
  your_score,comp_score=game(your_score,comp_score)

#final game scores
print('')
print(f'YOUR FINAL SCORE:{your_score}') 
print(f'COMPUTER FINAL SCORE:{comp_score}')

print('')
if(comp_score>your_score):
  print('COMPUTER WINS')
elif(comp_score<your_score):
  print('YOU WON')
else:
  print('GAME ENDED IN A DRAW')
print('')