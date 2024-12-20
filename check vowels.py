
sentence = input("Please type in a sentence: ")


lower_sentence = sentence.lower()


vowels = {'a', 'e', 'i', 'o', 'u'}

if vowels.issubset(lower_sentence):
   
    alphabet_list = [char for char in sentence if char.isalpha()]
    print("your sentence contain all the vowels")
    print("List of alphabets from your sentence:", alphabet_list)    
else:
    print("Your sentence does not contain all the vowels (a, e, i, o, u).")



