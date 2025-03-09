import tkinter as tk
import random

user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You Win!"
    return "Computer Wins!"

def play_game(user_choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    
    computer_choice_label.config(text=f"Computer Picked: {computer_choice}", fg="#FFEB3B")

    result = determine_winner(user_choice, computer_choice)

    if result == "You Win!":
        user_score += 1
        result_label.config(fg="#4CAF50")
    elif result == "Computer Wins!":
        computer_score += 1
        result_label.config(fg="#f44336")
    else:
        result_label.config(fg="#FFC107")

    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} | Computer {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    computer_choice_label.config(text="Computer Picked: ?", fg="white")
    result_label.config(text="Make Your Move!", fg="white")
    score_label.config(text="Score: You 0 | Computer 0")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x450")
root.configure(bg="#222831")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#222831", fg="#00ADB5")
title_label.pack(pady=15)

computer_choice_label = tk.Label(root, text="Computer Picked: ?", font=("Arial", 12), bg="#222831", fg="white")
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Make Your Move!", font=("Arial", 14, "bold"), bg="#222831", fg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 | Computer 0", font=("Arial", 12), bg="#222831", fg="white")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12, "bold"), width=10, bg="#FF5722", fg="white", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12, "bold"), width=10, bg="#03A9F4", fg="white", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12, "bold"), width=10, bg="#8BC34A", fg="white", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=15, command=reset_game)
reset_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="#555555", fg="white", width=15, command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
