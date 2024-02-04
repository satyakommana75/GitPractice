def highest_frequency_word_length(input_string):
    # Split the input string into words
    words = input_string.split()

    # Count the frequency of each word using a dictionary
    word_frequency = {}
    for word in words:
        # Remove non-alphanumeric characters from the word (e.g., punctuation)
        clean_word = ''.join(char for char in word if char.isalnum())

        # Increment the count for the cleaned word
        word_frequency[clean_word.lower()] = word_frequency.get(clean_word.lower(), 0) + 1

    # Find the word with the highest frequency
    max_frequency = 0
    max_frequency_word = ""
    for word, frequency in word_frequency.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_frequency_word = word

    # Return the length of the highest-frequency word
    return len(max_frequency_word)

# Example usage:
input_str = "This is a sample string. This string contains repeated words, and it may have repeated characters."
result = highest_frequency_word_length(input_str)
print("Length of the highest-frequency word:", result)