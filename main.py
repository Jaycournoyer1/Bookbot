def count_words(text):
    """Takes a string and returns the number of words."""
    words = text.split()  # Splitting the text into words
    return len(words)  # Returning word count

def count_characters(text):
    """Takes a string and returns a dictionary of character frequencies (case insensitive)."""
    text = text.lower()  # Convert text to lowercase
    char_count = {}  # Dictionary to store character frequencies
    
    for char in text:
        if char in char_count:
            char_count[char] += 1  # Increment count if character exists
        else:
            char_count[char] = 1  # Initialize count if character is new
    
    return char_count  # Return the character count dictionary

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  # Reading the book content
    
    word_count = count_words(file_contents)  # Call count_words function
    print("Total words in the book:", word_count)  # Print word count
    
    char_frequencies = count_characters(file_contents)  # Call count_characters function
    print("Character frequencies:", char_frequencies)  # Print character count dictionary

main()  # Run the main function