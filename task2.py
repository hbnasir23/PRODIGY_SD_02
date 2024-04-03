import random
import tkinter as tk

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    output_label.config(text="")
    guess_counter.config(text="Guesses: 0")
    submit_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x250")
root.configure(bg="teal")

# Variables
secret_number = random.randint(1, 100)
attempts = 0

# Styling
label_guess = tk.Label(root, text="Guess the Number (1-100):", bg="teal", fg="white", font=("Arial", 12, "bold"))
label_guess.pack(pady=(10, 0))

entry_guess = tk.Entry(root, font=("Arial", 12))
entry_guess.pack()

submit_button = tk.Button(root, text="Submit Guess", bg="grey", fg="white", font=("Arial", 12, "bold"))
submit_button.pack(pady=10)

output_label = tk.Label(root, text="", fg="blue", bg="teal", font=("Arial", 12))
output_label.pack()

guess_counter = tk.Label(root, text="Guesses: 0", fg="black", bg="teal", font=("Arial", 12))
guess_counter.pack()

play_again_button = tk.Button(root, text="Play Again", bg="green", fg="white", font=("Arial", 12, "bold"), command=reset_game)
play_again_button.pack(pady=10)
play_again_button.config(state=tk.DISABLED)

# Functions
def check_guess():
    global attempts
    guess = entry_guess.get().strip()
    entry_guess.delete(0, tk.END)
    attempts += 1

    try:
        guess = int(guess)
        if 1 <= guess <= 100:
            if guess == secret_number:
                output_label.config(text=f"Congratulations! You've guessed the number {secret_number} correctly!\nIt took you {attempts} attempts to win the game.", fg="yellow")
                submit_button.config(state=tk.DISABLED)
                play_again_button.config(state=tk.NORMAL)
            else:
                difference = abs(guess - secret_number)
                if difference <= 5:
                    feedback = "Close! Try again."
                elif guess < secret_number:
                    feedback = "Too low! Try again."
                else:
                    feedback = "Too high! Try again."

                output_label.config(text=feedback, fg="blue")

            guess_counter.config(text=f"Guesses: {attempts}")
        else:
            output_label.config(text="Please enter a number between 1 and 100.", fg="red")
    except ValueError:
        output_label.config(text="Please enter a valid number.", fg="red")

# Binding Enter key to submit the guess
def on_enter_key(event):
    check_guess()

root.bind('<Return>', on_enter_key)

# Configure the Submit button to call check_guess function
submit_button.config(command=check_guess)

root.mainloop()
