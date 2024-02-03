#checks if porfanity was found in text
def fudger():
    # Initializes user input and a query variable
    chat_box = input("Text Here: ")
    bad_words = ["damn", "hell", "shit"]
    
    # Split the user input into words
    words = chat_box.split()

    # Flag to track if any bad words were found
    bad_word_found = False

    # Loop through the words in the user input
    for i in range(len(words)):
        # If a bad word is found, replace it with fudge text
        if words[i] in bad_words:
            # Replace the bad word with a string of '*' characters of the same length
            words[i] = "*" * len(words[i])
            bad_word_found = True
        
    # Join the modified words back into a sentence
    fudged_chat = ' '.join(words)
    
    if bad_word_found:
        print("\n", fudged_chat)
        print("\nProfanity is not allowed!")
    else:
        print(fudged_chat)

fudger()
