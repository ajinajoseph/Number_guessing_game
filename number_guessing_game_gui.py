import tkinter as tk
import random

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x300")

num = 0
guess_count = 0
max_guesses = 10
low = 1
high = 100

def start_game():
    global num, guess_count
    num = random.randint(low, high)
    guess_count = 0
    result_label.config(text=f"Guess a number between {low} and {high}")
    entry.delete(0, tk.END)
    submit_button.config(state="normal")
    restart_button.config(state="disabled")

def check_guess():
    global guess_count
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    guess_count += 1

    if guess == num:
        result_label.config(text=f"🎉 Correct! You guessed it in {guess_count} tries.")
        submit_button.config(state="disabled")
        restart_button.config(state="normal")
    elif guess < num:
        result_label.config(text="Too low. Try a higher number.")
    else:
        result_label.config(text="Too high. Try a lower number.")

    if guess_count >= max_guesses and guess != num:
        result_label.config(text=f"❌ Game Over! The number was {num}.")
        submit_button.config(state="disabled")
        restart_button.config(state="normal")


title_label = tk.Label(window, text="🎯 Number Guessing Game", font=("Arial", 16))
title_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)

submit_button = tk.Button(window, text="Submit Guess", command=check_guess)
submit_button.pack(pady=5)

restart_button = tk.Button(window, text="Restart Game", command=start_game, state="disabled")
restart_button.pack(pady=5)

start_game()  # Initialize the game when the program starts
window.mainloop()

