def find_longest_and_smallest_words(sentence: str) -> tuple:
    """
    Finds the longest and smallest words in a sentence and their lengths.

    Args:
    sentence (str): The input sentence.

    Returns:
    tuple: The longest word with its length and the smallest word with its length.
    """
    words = sentence.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the longest word
    smallest_word = min(words, key=len)  # Find the smallest word
    return (longest_word, len(longest_word)), (smallest_word, len(smallest_word))


sentence = "Python is a versatile and powerful programming language"
(longest_word, longest_length), (smallest_word, smallest_length) = find_longest_and_smallest_words(sentence)

print(f"The longest word is '{longest_word}' with length {longest_length}.")
print(f"The smallest word is '{smallest_word}' with length {smallest_length}.")
