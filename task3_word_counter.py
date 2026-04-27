"""
========================================
Codveda Python Internship - Level 1
Task 3: Word Counter
Author  : Anselm Munango
Purpose : Read the contents of a plain-text file and produce a detailed
          word-count report including total words, unique words, sentence
          count, and the top 5 most frequently used words.
========================================
"""

import os
import re
from collections import Counter


# ------------------------------------------
# File reading
# ------------------------------------------

def read_file(file_path: str) -> str:
    """
    Read and return the full text content of a file.

    Args:
        file_path (str): Absolute or relative path to the target file.

    Returns:
        str: Raw text content of the file.

    Raises:
        FileNotFoundError : If the specified file does not exist.
        PermissionError   : If the application lacks read access.
        UnicodeDecodeError: If the file encoding is not UTF-8 compatible.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"The file '{file_path}' was not found. "
            "Please verify the path and try again."
        )

    with open(file_path, "r", encoding="utf-8") as fh:
        return fh.read()


# ------------------------------------------
# Analysis functions
# ------------------------------------------

def extract_words(text: str) -> list[str]:
    """
    Tokenise the text into lowercase alphabetic words, stripping punctuation.

    Args:
        text (str): Raw file content.

    Returns:
        list[str]: Ordered list of normalised word tokens.
    """
    return re.findall(r"[a-zA-Z']+", text.lower())


def count_sentences(text: str) -> int:
    """
    Estimate the number of sentences by counting terminal punctuation marks.

    Args:
        text (str): Raw file content.

    Returns:
        int: Approximate sentence count.
    """
    return len(re.findall(r"[.!?]+", text))


def analyse_text(text: str) -> dict:
    """
    Produce a comprehensive statistical summary of the file content.

    Args:
        text (str): Raw file content.

    Returns:
        dict: A dictionary containing all computed metrics.
    """
    words          = extract_words(text)
    word_count     = len(words)
    unique_words   = len(set(words))
    char_count     = len(text)
    char_no_space  = len(text.replace(" ", "").replace("\n", ""))
    line_count     = len(text.splitlines())
    sentence_count = count_sentences(text)
    top_words      = Counter(words).most_common(5)

    return {
        "total_words"    : word_count,
        "unique_words"   : unique_words,
        "total_characters": char_count,
        "chars_no_spaces": char_no_space,
        "total_lines"    : line_count,
        "total_sentences": sentence_count,
        "top_5_words"    : top_words,
    }


# ------------------------------------------
# Report renderer
# ------------------------------------------

def display_report(file_path: str, stats: dict) -> None:
    """
    Print a formatted word-count report to the console.

    Args:
        file_path (str): Path of the analysed file (used in the header).
        stats     (dict): Metrics dictionary returned by analyse_text().
    """
    print("\n" + "=" * 46)
    print("          WORD COUNT REPORT")
    print("=" * 46)
    print(f"  File               : {os.path.basename(file_path)}")
    print(f"  Total words        : {stats['total_words']:,}")
    print(f"  Unique words       : {stats['unique_words']:,}")
    print(f"  Total characters   : {stats['total_characters']:,}")
    print(f"  Chars (no spaces)  : {stats['chars_no_spaces']:,}")
    print(f"  Total lines        : {stats['total_lines']:,}")
    print(f"  Approx. sentences  : {stats['total_sentences']:,}")
    print("\n  Top 5 Most Frequent Words:")
    print("  " + "-" * 30)
    for rank, (word, freq) in enumerate(stats["top_5_words"], start=1):
        print(f"    {rank}. '{word}'  -  {freq} occurrence(s)")
    print("=" * 46 + "\n")


# ------------------------------------------
# Main application loop
# ------------------------------------------

def run_word_counter() -> None:
    """
    Prompt the user for a file path, perform the word-count analysis, and
    display the resulting report. Handles all common I/O exceptions gracefully.
    """
    print("\n" + "=" * 46)
    print("    WELCOME TO THE CODVEDA WORD COUNTER")
    print("=" * 46)

    while True:
        file_path = input("\n  Enter the path to a text file (or 'quit' to exit): ").strip()

        if file_path.lower() in ("quit", "exit", "q"):
            print("\n  Exiting Word Counter. Goodbye!\n")
            break

        try:
            content = read_file(file_path)

            if not content.strip():
                print("  The file is empty. Please provide a file with content.")
                continue

            stats = analyse_text(content)
            display_report(file_path, stats)

        except FileNotFoundError as error:
            print(f"\n  File Error    : {error}")
        except PermissionError:
            print(f"\n  Access Denied : You do not have permission to read '{file_path}'.")
        except UnicodeDecodeError:
            print(f"\n  Encoding Error: '{file_path}' could not be decoded as UTF-8.")
        except OSError as error:
            print(f"\n  OS Error      : {error}")


# ------------------------------------------
# Entry point
# ------------------------------------------

if __name__ == "__main__":
    run_word_counter()
