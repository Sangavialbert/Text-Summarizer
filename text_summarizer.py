import tkinter as tk
from tkinter import messagebox
import re
from collections import Counter

def summarize():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter a paragraph!")
        return

    sentences = re.split(r'(?<=[.!?])\s+', text)
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    stopwords = {
        "the", "is", "a", "an", "and", "of", "to", "in",
        "for", "on", "with", "this", "that", "are", "was",
        "as", "it", "by", "from", "be", "or", "at"
    }

    frequency = Counter(
        word for word in words if word not in stopwords
    )

    scores = {}

    for sentence in sentences:
        sentence_words = re.findall(
            r'\b[a-zA-Z]+\b', sentence.lower()
        )
        scores[sentence] = sum(
            frequency[word] for word in sentence_words
        )

    count = max(1, len(sentences) // 3)

    selected = sorted(
        sentences,
        key=lambda x: scores[x],
        reverse=True
    )[:count]

    summary = [s for s in sentences if s in selected]
    summary_text = " ".join(summary)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary_text)

    original_words = len(words)
    summary_words = len(
        re.findall(r'\b[a-zA-Z]+\b', summary_text)
    )

    word_label.config(
        text=f"Original Words: {original_words}   |   Summary Words: {summary_words}"
    )


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
    word_label.config(text="Original Words: 0   |   Summary Words: 0")


def copy_summary():
    summary = output_box.get("1.0", tk.END).strip()

    if summary:
        window.clipboard_clear()
        window.clipboard_append(summary)
        messagebox.showinfo("Copied", "Summary copied successfully!")
    else:
        messagebox.showwarning("Warning", "No summary to copy!")


# Main window
window = tk.Tk()
window.title("NLP Text Summarizer")
window.geometry("850x700")
window.resizable(False, False)

# Header
title = tk.Label(
    window,
    text="NLP TEXT SUMMARIZER",
    font=("Arial", 26, "bold")
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    window,
    text="Automatic Extractive Text Summarization",
    font=("Arial", 12)
)
subtitle.pack(pady=(0, 20))

# Input
input_label = tk.Label(
    window,
    text="Enter Your Paragraph",
    font=("Arial", 14, "bold")
)
input_label.pack()

input_box = tk.Text(
    window,
    height=11,
    width=90,
    font=("Arial", 11),
    wrap="word"
)
input_box.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

summarize_button = tk.Button(
    button_frame,
    text="SUMMARIZE",
    font=("Arial", 12, "bold"),
    padx=25,
    pady=8,
    command=summarize
)
summarize_button.grid(row=0, column=0, padx=8)

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    padx=25,
    pady=8,
    command=clear_text
)
clear_button.grid(row=0, column=1, padx=8)

copy_button = tk.Button(
    button_frame,
    text="COPY SUMMARY",
    font=("Arial", 12, "bold"),
    padx=25,
    pady=8,
    command=copy_summary
)
copy_button.grid(row=0, column=2, padx=8)

# Output
output_label = tk.Label(
    window,
    text="Generated Summary",
    font=("Arial", 14, "bold")
)
output_label.pack(pady=(15, 5))

output_box = tk.Text(
    window,
    height=9,
    width=90,
    font=("Arial", 11),
    wrap="word"
)
output_box.pack(pady=10)

# Word count
word_label = tk.Label(
    window,
    text="Original Words: 0   |   Summary Words: 0",
    font=("Arial", 11, "bold")
)
word_label.pack(pady=10)

# Footer
footer = tk.Label(
    window,
    text="NLP Mini Project • Text Summarization",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=15)

window.mainloop()