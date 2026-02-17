import tkinter as tk
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Learning App")
        self.root.geometry("400x300")

        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Python data type for unordered key-value pairs?", "answer": "Dictionary"},
            {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
            {"question": "Shortcut for copying text?", "answer": "Ctrl + C"}
        ]

        random.shuffle(self.flashcards)

        self.current_index = 0
        self.showing_answer = False

        self.card_text = tk.StringVar()
        self.card_text.set(self.flashcards[self.current_index]["question"])

        tk.Label(root, text="Flashcard Learning",
                 font=("Arial", 14, "bold")).pack(pady=10)

        self.card_label = tk.Label(
            root,
            textvariable=self.card_text,
            wraplength=350,
            font=("Arial", 12),
            bg="white",
            width=40,
            height=5,
            relief="solid"
        )
        self.card_label.pack(pady=20)

        tk.Button(root, text="Flip",
                  command=self.flip_card).pack(pady=5)

        tk.Button(root, text="Next",
                  command=self.next_card).pack(pady=5)

    def flip_card(self):
        self.showing_answer = not self.showing_answer
        if self.showing_answer:
            self.card_text.set(
                self.flashcards[self.current_index]["answer"])
        else:
            self.card_text.set(
                self.flashcards[self.current_index]["question"])

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.showing_answer = False
        self.card_text.set(
            self.flashcards[self.current_index]["question"])


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
