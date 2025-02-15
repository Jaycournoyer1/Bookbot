def count_words(text):
    """Takes a string and returns the number of words."""
    words = text.split()  # Splitting the text into words
    return len(words)  # Returning word count

def count_characters(text):
    """Takes a string and returns a dictionary of character frequencies (case insensitive)."""
    text = text.lower()  # Convert text to lowercase
    char_count = {}  # Dictionary to store character frequencies
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1  # Increment count if character exists
            else:
                char_count[char] = 1  # Initialize count if character is new
    
    return char_count  # Return the character count dictionary

def sort_on(dict):
    """Helper function to sort a list of dictionaries by the 'num' key."""
    return dict["num"]

def generate_report(filename, word_count, char_frequencies):
    """Prints a formatted report of the word and character frequency data."""
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")

    # Convert the dictionary into a sorted list of dictionaries
    sorted_chars = [{"char": char, "num": count} for char, count in char_frequencies.items()]
    sorted_chars.sort(reverse=True, key=sort_on)  # Sort by character frequency (descending)

    # Print character frequencies
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        file_contents = f.read()  # Reading the book content
    
    word_count = count_words(file_contents)  # Get word count
    char_frequencies = count_characters(file_contents)  # Get character frequency count
    
    generate_report(filename, word_count, char_frequencies)  # Generate and print the report

main()  # Run the main function