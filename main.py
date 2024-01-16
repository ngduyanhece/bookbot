# function to read the text file from books 
def read_book(filename):
		"""Reads a book and returns it as a string.

		Args:
				filename: The name of the file to read.

		Returns:
				str: The contents of the file as a string.
		"""

		with open(filename, "r") as file:  # Open the file for reading
				text = file.read()  # Read the contents of the file
		return text  # Return the contents of the file

def count_words(text):
		"""Counts the number of words in the given text.

		Args:
				text: A string containing the text to be analyzed.

		Returns:
				int: The number of words in the text.
		"""

		words = text.split()  # Split the text into words based on whitespace
		return len(words)  # Return the number of words in the list

def count_letters(text):
    """Counts the occurrences of each letter in the given text.

    Args:
        text: A string containing the text to be analyzed.

    Returns:
        dict: A dictionary mapping each letter (lowercase) to its count in the text.
    """

    letter_counts = {}  # Initialize an empty dictionary
    for char in text.lower():  # Iterate over characters in lowercase
        if char.isalpha():  # Check if it's a letter
            letter_counts[char] = letter_counts.get(char, 0) + 1  # Count occurrences
    return letter_counts

def print_book_report(book_path):
    """Prints a formatted report of word and letter counts for a given book."""

    with open(book_path, "r") as book_file:
        book_text = book_file.read()

    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)

    print("--- Begin report of", book_path, "---")
    print(f"{word_count} words found in the document")
    print("\nThe character counts are as follows:")

    for letter, count in sorted(letter_counts.items()):
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

# Example usage
print_book_report("books/frankenstein.txt")  # Replace with your book's path


# Example usage
if __name__ == "__main__":
	book_text = read_book("books/frankenstein.txt")
	word_count = count_words(book_text)
	print("Number of words in the book:", word_count)  # Print the word count
	letter_counts = count_letters(book_text)
	print("Number of times each letter occurs:", letter_counts)  # Print the letter counts
	print_book_report("books/frankenstein.txt")  # Print the book report
