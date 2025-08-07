import tkinter as tk         # Importing libraries
from random import choice
import time

class TypingTest:            # Main class that creates GUI and handles th speed typing test logic
    def __init__(self):      # Constructor of class which set up neccesary variables
        self.root = tk.Tk()  # GUI method
        self.root.title("Speed Typing Test")

        self.texts = [       # Define a sentence for the user to type 
            "The quick brown fox jumps over the lazy dog",
            "The sun is shining brightly in the clear blue sky.",
            "The birds are singing their sweet melodies."     
        ]

        self.text_to_type = tk.StringVar()
        self.text_to_type.set(choice(self.texts))

        self.typed_text = tk.StringVar()
        self.accuracy = tk.StringVar()
        self.wpm = tk.StringVar()
        self.elapsed_time = tk.StringVar()

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Type the following text:").pack()
        tk.Label(self.root, textvariable=self.text_to_type, wraplength=400, font=("Arial", 14)).pack()
    
        tk.Entry(self.root, textvariable=self.typed_text,font=("Arial",14)).pack()

        tk.Button(self.root, text="Start", command=self.start_test).pack()
        tk.Button(self.root, text="Submit", command=self.calculate_results).pack()

        tk.Label(self.root, text="Accuracy:").pack()
        tk.Label(self.root, textvariable=self.accuracy).pack()

        tk.Label(self.root, text="Words per minute (wpm):").pack()
        tk.Label(self.root, textvariable=self.wpm).pack()

        tk.Label(self.root, text="Elapsed time (seconds):").pack()
        tk.Label(self.root, textvariable=self.elapsed_time).pack()

    def start_test(self):          # This method is called when start button is clicked
        self.start_time = time.time()
        self.typed_text.set("")

    def calculate_results(self):   # This method is called when submit button is clicked
        elapsed_time = time.time() - self.start_time
        accuracy = self.calculate_accuracy(self.text_to_type.get(), self.typed_text.get())
        wpm = self.calculate_wpm(self.typed_text.get(), elapsed_time)

        self.accuracy.set(f"Accuracy: {accuracy:.2f}%")
        self.wpm.set(f"WPM: {wpm:.2f}")
        self.elapsed_time.set(f"Elapsed time: {elapsed_time:.2f} seconds")

    def calculate_accuracy(self, original_text, typed_text):  # This method calculates the accuracy of typed text
        original_words = original_text.split()
        typed_words = typed_text.split()
        correct_words = sum(1 for i in range(min(len(original_words), len(typed_words))) if original_words[i] == typed_words[i])
        return (correct_words / len(original_words)) * 100

    def calculate_wpm(self, typed_text, elapsed_time): # Calculates the words per minute
        num_words = len(typed_text.split())
        return (num_words / elapsed_time) * 60

    def run(self):    # This method starts the GUI event loop using 'main loop '
        self.root.mainloop()

if __name__ == "__main__":   # Main script creates an instance of typing test class and calls its run method
    test = TypingTest()
    test.run()

