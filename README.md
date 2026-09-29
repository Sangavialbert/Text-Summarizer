# NLP-Based Automatic Text Summarization System

## 📌 Project Overview

This project is an **NLP-based Automatic Text Summarization System** developed using Python.

The system takes a long paragraph as input and generates a shorter summary by identifying and extracting the most important sentences based on word frequency.

It provides a simple graphical user interface (GUI) using Tkinter.

## 🎯 Objectives

- To understand basic Natural Language Processing concepts.
- To preprocess and analyze text data.
- To identify important words and sentences.
- To generate an automatic summary from a paragraph.
- To provide an easy-to-use graphical interface.

## 🛠️ Technologies Used

- **Python**
- **Natural Language Processing (NLP)**
- **Tkinter**
- **Regular Expressions**
- **Counter / Word Frequency Analysis**

## ⚙️ How It Works

The system follows these steps:

1. The user enters a paragraph.
2. The text is divided into individual sentences.
3. Words are extracted from the text.
4. Common stopwords are removed.
5. The frequency of important words is calculated.
6. Each sentence is given a score based on word frequency.
7. The highest-scoring sentences are selected.
8. The selected sentences are arranged in their original order.
9. The final summary is displayed to the user.

## ✨ Features

- 📝 Paragraph input
- 🤖 Automatic text summarization
- 📊 Original and summary word count
- 📋 Copy Summary button
- 🧹 Clear button
- 🖥️ User-friendly GUI
- ⚡ Fast text processing

## 📂 Project Structure

```text
NLP_Project/
│
├── text_summarizer.py
├── sentiment_analyzer.py
└── README.md
