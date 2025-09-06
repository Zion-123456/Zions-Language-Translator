from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator  # ✅ keep it as googletrans, not googletrans_py

# Initialize main window
root = Tk()
root.title("Language Translator")
root.geometry("700x500")  # ✅ larger window
root.resizable(False, False)

# Translator object
translator = Translator()

# Available languages (expanded)
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Yoruba": "yo",
    "Igbo": "ig",
    "Hausa": "ha",
}


# Function to translate text
def translate_text():
    try:
        input_text = input_box.get("1.0", END).strip()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate")
            return

        src_lang = languages[source_lang.get()]
        dest_lang = languages[target_lang.get()]

        translation = translator.translate(input_text, src=src_lang, dest=dest_lang)
        output_box.delete("1.0", END)
        output_box.insert(END, translation.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


# UI Layout
Label(root, text="Enter Text:", font=("Arial", 14, "bold")).pack(pady=8)

input_box = Text(root, height=8, width=80, wrap=WORD, font=("Arial", 12))
input_box.pack(pady=8)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="From:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly", font=("Arial", 12), width=20)
source_lang.set("English")
source_lang.grid(row=0, column=1, padx=5)

Label(frame, text="To:", font=("Arial", 12)).grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=list(languages.keys()), state="readonly", font=("Arial", 12), width=20)
target_lang.set("French")
target_lang.grid(row=0, column=3, padx=5)

Button(root, text="Translate", command=translate_text, bg="blue", fg="white",
       font=("Arial", 14, "bold"), width=15).pack(pady=12)

Label(root, text="Translated Text:", font=("Arial", 14, "bold")).pack(pady=8)

output_box = Text(root, height=8, width=80, wrap=WORD, font=("Arial", 12))
output_box.pack(pady=8)

root.mainloop()
