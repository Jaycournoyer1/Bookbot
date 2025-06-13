def get_num_words(text):
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
