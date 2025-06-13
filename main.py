import sys
from stats import (
    get_num_words,
    count_characters,
    sort_on
)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    filename = sys.argv[1]  # Get the filename from command line arguments
    with open(filename) as f:
        file_contents = f.read()  # Reading the book content
    
    word_count = get_num_words(file_contents)  # Get word count
    char_frequencies = count_characters(file_contents)  # Get character frequency count
    
    generate_report(filename, word_count, char_frequencies)  # Generate and print the report

def generate_report(filename, word_count, char_frequencies):
    """Prints a formatted report of the word and character frequency data."""
    print(f"--- Begin report of {filename} ---")
    print(f"Found {word_count} total words\n")

    # Convert the dictionary into a sorted list of dictionaries
    sorted_chars = [{"char": char, "num": count} for char, count in char_frequencies.items()]
    sorted_chars.sort(reverse=True, key=sort_on)  # Sort by character frequency (descending)

    # Print character frequencies
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("--- End report ---")
    
main()  # Run the main function