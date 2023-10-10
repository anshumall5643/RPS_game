#ROCK, PAPER AND SCISSORS GAME
from random import randint
t = ["Rock", "Paper", "Scissors"] #list of choice options
comp_choice = t[randint(0,2)]  #random choice for computer

your_choice =1
computer_win=0
player_win=0

while your_choice == 1:
#player chooses its option
    your_choice = input("Chose Rock, Paper, Scissors? ")
    comp_choice = t[randint(0,2)]
    if your_choice == comp_choice:
        print("Both choose the same",comp_choice)
    
    elif your_choice == "Rock":
        if comp_choice == "Paper":
            print("computer choose", comp_choice, "player choose", your_choice)
            computer_win+=1
            
        else:
            print("player choose", your_choice, "computer choose", comp_choice)
            player_win+=1   

    elif your_choice == "Paper":
        if comp_choice == "Scissors":
            print("computer choose", comp_choice, "player choose", your_choice)
            computer_win+=1
        else:
            print("player choose", your_choice, "computer choose", comp_choice)
            player_win+=1
            
    elif your_choice == "Scissors":
        if comp_choice == "Rock":
            print("\tcomputer choose", comp_choice, "player choose", your_choice)
            computer_win+=1            
        else:
            print("\tplayer choose", your_choice, "computer choose", comp_choice)
            player_win+=1
            
    else:
        print("That's not a valid play. Check your spelling!")
    
    print()

    ch = input("do you wish to continue(y/n)") #choice for continuing loop
    if ch=="y":
       your_choice=1 
    else:
       break
print()
if(computer_win>player_win):
 print('Finally computer Win!')
elif(computer_win<player_win):
 print('Finally You Win!')
else:
 print('Tie Scores!')
print()
print("\n\tScore:")
print("\n \tcomputer score:",computer_win)
print("\t player score:",player_win)'''
