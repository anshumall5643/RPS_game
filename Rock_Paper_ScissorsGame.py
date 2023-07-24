import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "Congratulations! You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")
    root.geometry("400x200")
    root.configure(bg="#F5E1DA")  # Set background color

    custom_font = ("Helvetica", 14)

    label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=custom_font, fg="#333", bg="#F5E1DA")
    label.pack(pady=20)

    button_frame = tk.Frame(root, bg="#F5E1DA")
    button_frame.pack()

    rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"), font=custom_font, fg="white", bg="#0074D9", activebackground="#0056b3")
    rock_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"), font=custom_font, fg="white", bg="#FF4136", activebackground="#E01B17")
    paper_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"), font=custom_font, fg="white", bg="#2ECC40", activebackground="#23923A")
    scissors_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()






'''import tkinter as tk
from random import randint

class RockPaperScissorsGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rock, Paper, Scissors Game")
        self.geometry("400x300")
        self.configure(bg="#F5E1DA")  # Set background color

        # Center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry("+{}+{}".format(x, y))

        self.result_label = tk.Label(self, text="Chose Rock, Paper, or Scissors?", bg="#F5E1DA", fg="#333", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.your_choice = None
        self.computer_win = 0
        self.player_win = 0

        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play_game("Rock"), bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play_game("Paper"), bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self, text="Scissors", command=lambda: self.play_game("Scissors"), bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    def play_game(self, your_choice):
        t = ["Rock", "Paper", "Scissors"]  # list of choice options
        comp_choice = t[randint(0, 2)]  # random choice for computer

        if your_choice == comp_choice:
            self.result_label.config(text="Both choose the same: {}".format(comp_choice), fg="#333")
        elif your_choice == "Rock":
            if comp_choice == "Paper":
                self.result_label.config(text="Computer choose {}, You choose {}. Computer wins!".format(comp_choice, your_choice), fg="red")
                self.computer_win += 1
            else:
                self.result_label.config(text="You choose {}, Computer choose {}. You win!".format(your_choice, comp_choice), fg="#3D9970")
                self.player_win += 1
        elif your_choice == "Paper":
            if comp_choice == "Scissors":
                self.result_label.config(text="Computer choose {}, You choose {}. Computer wins!".format(comp_choice, your_choice), fg="red")
                self.computer_win += 1
            else:
                self.result_label.config(text="You choose {}, Computer choose {}. You win!".format(your_choice, comp_choice), fg="#3D9970")
                self.player_win += 1
        elif your_choice == "Scissors":
            if comp_choice == "Rock":
                self.result_label.config(text="Computer choose {}, You choose {}. Computer wins!".format(comp_choice, your_choice), fg="red")
                self.computer_win += 1
            else:
                self.result_label.config(text="You choose {}, Computer choose {}. You win!".format(your_choice, comp_choice), fg="#3D9970")
                self.player_win += 1

    def reset(self):
        self.computer_win = 0
        self.player_win = 0
        self.result_label.config(text="Chose Rock, Paper, or Scissors?", fg="#333")

if __name__ == "__main__":
    app = RockPaperScissorsGame()
    app.mainloop()
'''


'''#ROCK, PAPER AND SCISSORS GAME
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