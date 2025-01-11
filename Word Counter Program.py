# Word Counter Program
# Week 2 Python Programming Internship Project

# Function to count the number of words in the input text
def count_words(text):
    """Counts the number of words in the given text."""
    # Split the text by spaces and count the resulting list elements
    words = text.split()
    return len(words)

# Main Program
if __name__ == "__main__":
    print("Welcome to the Word Counter Program!\n")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty input. Please try again.")
    else:
        # Count the words using the count_words function
        word_count = count_words(user_input)

        # Display the word count to the user
        print("\nThe total number of words in the entered text is:", word_count)

    print("\nThank you for using the Word Counter Program!")
