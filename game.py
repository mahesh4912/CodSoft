import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    
    # Computer randomly selects rock, paper, or scissors
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    # Update result labels
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again()

# Function to ask the user if they want to play again
def play_again():
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        # Reset the result labels for a new round
        user_choice_label.config(text="Your Choice: ")
        computer_choice_label.config(text="Computer's Choice: ")
        result_label.config(text="")
    else:
        root.quit()

# Create the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x500")  # Size of the window
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Create and place widgets
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 24, "bold"), bg="#34495e", fg="white")
title_label.pack(pady=20)

# Frame for user buttons
button_frame = tk.Frame(root, bg="#34495e")
button_frame.pack(pady=20)

# Buttons for user choices
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 16), command=lambda: determine_winner("Rock"), bg="#e74c3c", fg="white", padx=20, pady=10)
rock_button.grid(row=0, column=0, padx=20)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 16), command=lambda: determine_winner("Paper"), bg="#3498db", fg="white", padx=20, pady=10)
paper_button.grid(row=0, column=1, padx=20)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 16), command=lambda: determine_winner("Scissors"), bg="#2ecc71", fg="white", padx=20, pady=10)
scissors_button.grid(row=0, column=2, padx=20)

# Labels to display choices and result
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 18), bg="#34495e", fg="white")
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 18), bg="#34495e", fg="white")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 22, "bold"), bg="#34495e", fg="white")
result_label.pack(pady=20)

# Label to display the score
score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Helvetica", 18), bg="#34495e", fg="white")
score_label.pack(pady=20)

# Button to play again
play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 16), command=play_again, bg="#e67e22", fg="white", padx=20, pady=10)
play_again_button.pack(pady=10)

# Start the application
root.mainloop()
