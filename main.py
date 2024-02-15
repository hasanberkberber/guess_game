import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)

        self.label = tk.Label(self.master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.check_button = tk.Button(self.master, text="Check", command=self.check_guess)
        self.check_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        if guess < self.secret_number:
            self.result_label.config(text="Too low!")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high!")
        else:
            self.result_label.config(text="Congratulations! You guessed it!")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.result_label.config(text="")
        self.entry.delete(0, 'end')


def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    print("Program started...")
    main()