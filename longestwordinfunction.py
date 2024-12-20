def find_longest_word(sentence: str) -> tuple:
   
    words = sentence.split()  
    longest_word = max(words , key=len)
    return longest_word, len(longest_word)  


sentence = input('enter the sentence:')
word, length = find_longest_word(sentence)

print(f"The longest word is '{word}' with length is : {length}.")
