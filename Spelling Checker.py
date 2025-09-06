from tkinter import *
from tkinter import messagebox
from textblob import TextBlob
import os

# Dictionary file
DICT_FILE = "custom_dict.txt"

# Load custom dictionary
if os.path.exists(DICT_FILE):
    with open(DICT_FILE, "r") as f:
        custom_dict = set(f.read().splitlines())
else:
    custom_dict = set()

# Function to check spelling
def check_spelling():
    global last_word
    word = entry.get().strip()
    last_word = word  # store for possible "Add to Dictionary"

    if not word:
        messagebox.showwarning("Input Error", "Please enter a word to check")
        return

    # If word already in custom dictionary → accept as correct
    if word.lower() in custom_dict:
        result_label.config(text=f"✅ '{word}' is in your custom dictionary!", fg="green")
        return

    blob = TextBlob(word)
    corrected_word = str(blob.correct())

    if word.lower() == corrected_word.lower():
        result_label.config(text=f"✅ '{word}' is spelled correctly!", fg="green")
    else:
        result_label.config(
            text=f"❌ '{word}' is incorrect. Did you mean '{corrected_word}'?",
            fg="red"
        )

# Function to add word to dictionary
def add_to_dictionary():
    global last_word
    word = entry.get().strip()

    if not word:
        messagebox.showwarning("Input Error", "Please enter a word first")
        return

    # Save to custom dictionary
    custom_dict.add(word.lower())
    with open(DICT_FILE, "a") as f:
        f.write(word.lower() + "\n")

    messagebox.showinfo("Dictionary Updated", f"'{word}' added to your dictionary!")
    result_label.config(text=f"📘 '{word}' is now recognized as correct.", fg="blue")

# Main window
root = Tk()
root.title("Spelling Checker with Dictionary")
root.geometry("600x300")
root.resizable(False, False)

# UI elements
Label(root, text="Enter a word:", font=("Arial", 14)).pack(pady=10)

entry = Entry(root, font=("Arial", 14), width=25, justify="center")
entry.pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="Check Spelling", command=check_spelling,
       bg="blue", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=0, padx=10)

Button(frame, text="Add to Dictionary", command=add_to_dictionary,
       bg="green", fg="white", font=("Arial", 12, "bold"), width=15).grid(row=0, column=1, padx=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
