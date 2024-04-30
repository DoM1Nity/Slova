import tkinter as tk
from tkinter import messagebox
import string
import random

class MaailmaMäng:
    def __init__(self, master):
        self.master = master
        self.master.title("Maailma Mäng")

        self.load_word_list("sõnu.txt")
        self.new_game()

        self.create_widgets()

    def load_word_list(self, filename):
        with open(filename, 'r') as file:
            self.word_list = [line.strip().upper() for line in file]

    def new_game(self):
        self.secret_word = random.choice(self.word_list)
        self.remaining_attempts = 5
        self.guessed_letters = set()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="Enter a 5-letter word:", font=("Arial", 16))
        self.word_label.grid(row=0, column=0, columnspan=2, pady=10 )

        self.input_entry = tk.Entry(self.master, font=("Arial", 16), width=10)
        self.input_entry.grid(row=1, column=0, columnspan=2, pady=5)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess, font=("Arial", 14))
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.remaining_attempts_label = tk.Label(self.master, text=f"Attempts left: {self.remaining_attempts}",
                                                 font=("Arial", 16))
        self.remaining_attempts_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.alphabet_label = tk.Label(self.master, text="Alphabet:", font=("Arial", 16))
        self.alphabet_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.alphabet_buttons = []
        for i, letter in enumerate(string.ascii_uppercase):
            row = i // 5 + 5
            col = i % 5
            button = tk.Button(self.master, text=letter, font=("Arial", 14), command=lambda l=letter: self.select_letter(l))
            button.grid(row=row, column=col, padx=3, pady=3)
            self.alphabet_buttons.append(button)

    def select_letter(self, letter):
        self.input_entry.insert(tk.END, letter)

    def check_guess(self):
        guess = self.input_entry.get().upper()
        self.input_entry.delete(0, tk.END)

        if len(guess) != 5 or not guess.isalpha():
            messagebox.showwarning("Vigane sisend", " palun sisestage kehtiv 5-täheline sõna.")
            return

        self.remaining_attempts -= 1
        self.remaining_attempts_label.config(text=f"Katsed vasakule: {self.remaining_attempts}")

        if guess == self.secret_word:
            messagebox.showinfo("Palju õnne!", f" sa arvasid sõna: {self.secret_word}")
            self.new_game()
            self.remaining_attempts_label.config(text=f"Katsed vasakule: {self.remaining_attempts}")
        else:
            if self.remaining_attempts == 0:
                messagebox.showinfo("Mäng Läbi", f"Välja katsed! Sõna oli: {self.secret_word}")
                self.new_game()
                self.remaining_attempts_label.config(text=f"Katsed vasakule: {self.remaining_attempts}")

def main():
    root = tk.Tk()
    root.geometry("500x570")
    game = MaailmaMäng(root)
    root.mainloop()

if __name__ == "__main__":
    main()

