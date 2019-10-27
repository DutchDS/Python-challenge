import string
import os

word_count = 0
sentence_count = 0
letter_count = 0
average_word = 0.00
AR_Check = 0

#For our letter count we only count letters in the alphabet - ommitting special characters.
letters = string.ascii_lowercase

#Since we have 2 input files that need to be processed, loop twice
i = 1
while i <= 2: 
    my_text_path = os.path.join('raw_data', 'paragraph_' + str(i) + '.txt')
    text = open(my_text_path, "r") 
    for each_line in text: 
        # Move each word (indicated by a " "-separator) into a list called 'words' and get it's length to find the word count
        words = each_line.split(" ")
        word_count = word_count + len(words)

        #Move each sentence (indicated by a '.') into a list called sentences and use it's lenght to find the sentence count.
        sentences = each_line.split(".")
        sentence_count = sentence_count + len(sentences) - 1

        #For our letter count, first remove all spaces
        text_nospace = each_line.replace(" ", "")
        #Then make sure everything is lowercase
        text_lower = text_nospace.lower()
        #Finally remove any special characters as defined by spring.punctuation
        text_nopunctuation = text_lower.strip(string.punctuation)
        #For each letter (a) in the alphabet, count the number of occurences and add them up
        for a in letters:
            if a in text_nopunctuation:
                per_letter_count = text_nopunctuation.count(a)
                letter_count = per_letter_count + letter_count
                #print(a, letter_count)
        
        #Compute averages
        average_word = round(letter_count/word_count,2)
        average_sentence = round(word_count/sentence_count,0)
        
    #Output results to screen
    print("*********************************")
    print("Paragraph" + str(i) + " Analysis" )
    print("---------------------------------")
    print(f'Approximate word count: {word_count}')
    print(f'Approximate sentence count: {sentence_count}')            
    print(f'Average Letter count: {average_word}')
    print(f'Average sentence length: {average_sentence}')
    #print(f'Letter count: {letter_count}')
    print("---------------------------------")

    #Move to next Paragraph and reset counters
    i = i + 1
    word_count = 0
    sentence_count = 0
    letter_count = 0
    average_word = 0.00