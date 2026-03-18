# Bookbot

A Python command-line tool that analyzes text files and generates word and character frequency reports.

## Overview

Bookbot processes raw text and turns it into structured, readable output directly from the terminal. It is designed as a simple utility for quickly understanding patterns in a text file without needing external tools.

## What It Does

- Counts total words in a text file  
- Tracks frequency of each word  
- Tracks frequency of each character  
- Outputs sorted results for easy reading  

## Example Use Case

If you have a large text file (book, article, dataset), Bookbot helps answer questions like:

- What words appear most often?
- How frequently are certain characters used?
- What patterns exist in the text?

## How It Works

Bookbot follows a simple data flow:

Input (text file) → Processing (count + organize) → Output (sorted report)

- Reads a .txt file  
- Parses text into words and characters  
- Uses dictionaries to store counts  
- Sorts results for readability  
- Prints a formatted report to the CLI  

## Installation

Clone the repository:

git clone https://github.com/villadv/bookbot.git
cd bookbot

Make sure you have Python installed (3.x recommended).

## Usage

Run the script with a text file:

python main.py <path_to_text_file>

Example:

python main.py books/frankenstein.txt

## Sample Output

--- Begin report ---
Total words: 78321

Character frequency:
e: 44538
t: 29493
a: 25894

Top words:
the: 8000
and: 6200
to: 5000
--- End report ---

## Demo

![Bookbot CLI Output](images/bookbot-output.png)

## What I Learned

- Structuring a small application end-to-end  
- Processing and organizing data using dictionaries  
- Sorting complex data structures for readability  
- Thinking in terms of input → process → output  

## Future Improvements

- Export results to CSV  
- Support multiple input files  
- Add filtering (ignore stop words, case normalization)  
- Extend into a simple text-processing pipeline  

## License

MIT
