# 📝 Word Counter — Codeveda Python Internship

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Internship](https://img.shields.io/badge/Internship-Codeveda-green?style=flat-square)
![Level](https://img.shields.io/badge/Level-1-brightgreen?style=flat-square)
![Task](https://img.shields.io/badge/Task-3-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

> A Python text-analysis tool that reads any plain-text file and produces a structured word-count report — covering total words, unique vocabulary, sentence count, and the top 5 most frequently used terms.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Technical Architecture](#technical-architecture)
- [Function Reference](#function-reference)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Author](#author)

---

## Overview

This project was developed as **Task 3** of the **Codeveda Python Internship – Level 1**. It implements a file-based text analyser that reads the full content of a plain-text file and produces a comprehensive word-count report through a series of modular, type-annotated functions.

The tool leverages Python's standard library — `os`, `re`, and `collections.Counter` — to perform efficient text parsing, pattern matching, and frequency analysis without any third-party dependencies.

---

## ✨ Features

- ✅ Reads and validates any plain-text (`.txt`) file via file path
- ✅ Counts **total words** using regex-based tokenisation
- ✅ Counts **unique words** (case-insensitive deduplication)
- ✅ Counts **sentences** using punctuation-aware pattern matching
- ✅ Identifies the **Top 5 most frequently used words** via `collections.Counter`
- ✅ Excludes common stop words from frequency rankings
- ✅ Displays a clean, structured report to the console
- ✅ Graceful error handling for missing or unreadable files

---

## 📁 Project Structure

```
Codeveda_task3_word_counter.py/
│
└── task3_word_counter.py    # Main analysis module (180 lines, 142 loc · 5.44 KB)
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/f-anselm88/Codeveda_task3_word_counter.py.git
```

2. Navigate into the project directory:

```bash
cd Codeveda_task3_word_counter.py
```

3. Run the analyser against any `.txt` file:

```bash
python task3_word_counter.py
```

No external packages required — built entirely on the Python standard library.

---

## 💻 Usage

When executed, the program prompts the user to provide the path to a plain-text file. It then processes the file and prints a formatted analysis report.

```bash
python task3_word_counter.py
Enter the path to your text file: sample.txt
```

You can also adapt `task3_word_counter.py` to import its functions directly into another module:

```python
from task3_word_counter import read_file, count_words, count_sentences, top_words

text = read_file("my_document.txt")
print(count_words(text))
print(top_words(text, n=5))
```

---

## 📊 Sample Output

```
============================================================
           WORD COUNT REPORT
============================================================
  File            : sample.txt
  Total Words     : 312
  Unique Words    : 198
  Sentences       : 24
------------------------------------------------------------
  Top 5 Most Frequent Words:
    1. python        —  18 occurrences
    2. function      —  14 occurrences
    3. data          —  11 occurrences
    4. program       —   9 occurrences
    5. variable      —   7 occurrences
============================================================
```

---

## 🏗️ Technical Architecture

### Module Dependencies

```
task3_word_counter.py
    │
    ├── os                        # File path validation and existence checks
    ├── re                        # Regex tokenisation for words and sentences
    └── collections.Counter       # Frequency ranking of word occurrences
```

### Processing Pipeline

```
User Input (file path)
    │
    ▼
read_file()           ── Validates path, reads raw text content
    │
    ▼
count_words()         ── Tokenises text via regex; returns total word count
    │
    ▼
count_unique_words()  ── Lowercases tokens; returns unique vocabulary size
    │
    ▼
count_sentences()     ── Detects sentence boundaries (. ! ?) via regex
    │
    ▼
top_words()           ── Filters stop words; ranks by Counter frequency
    │
    ▼
display_report()      ── Formats and prints the final structured report
```

---

## 📖 Function Reference

| Function | Signature | Description |
|---|---|---|
| `read_file` | `read_file(file_path: str) -> str` | Reads and returns the full text content of the specified file |
| `count_words` | `count_words(text: str) -> int` | Returns the total word count using regex tokenisation |
| `count_unique_words` | `count_unique_words(text: str) -> int` | Returns the number of unique words (case-insensitive) |
| `count_sentences` | `count_sentences(text: str) -> int` | Returns the sentence count based on `.` `!` `?` delimiters |
| `top_words` | `top_words(text: str, n: int) -> list` | Returns the `n` most frequent words, excluding stop words |
| `display_report` | `display_report(file_path: str, text: str) -> None` | Prints the full formatted analysis report to the console |

---

## 🧠 Concepts Demonstrated

This project showcases the following Python programming skills:

- **File I/O** — reading external files using `open()` with context managers and encoding handling
- **Regular Expressions (`re`)** — pattern-based word tokenisation and sentence boundary detection
- **`collections.Counter`** — efficient frequency analysis of word occurrences
- **String manipulation** — lowercasing, stripping punctuation, and stop-word filtering
- **Type annotations** — all functions use `str`, `int`, and `list` return type hints
- **Modular design** — each analytical step is encapsulated in a single-responsibility function
- **Error handling** — `FileNotFoundError` and `IOError` managed with informative messages
- **`os` module** — file path validation using `os.path.exists()` and `os.path.isfile()`

---

## 👤 Author

**Anselm Munango**
- GitHub: [@f-anselm88](https://github.com/f-anselm88)
- Programme: Codeveda Python Internship – Level 1

---

*Built as part of a structured internship programme to demonstrate applied Python skills in file handling, text processing, and data analysis.*
