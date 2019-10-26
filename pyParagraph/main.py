import string
import os

word_count = 0
sentence_count = 0
letter_count = 0
average_word = 0.00

letters = string.ascii_lowercase

i = 1
while i <= 2:
    my_text_path = os.path.join('raw_data', 'paragraph_' + str(i) + '.txt')
    text = open(my_text_path, "r") 
    for line in text: 
        # Remove the leading spaces and newline character 
        words = line.split(" ")
        word_count = word_count + len(words)

        sentences = line.split(".")
        sentence_count = sentence_count + len(sentences) - 1

        text_nospace = line.replace(" ", "")
        text_nopunctuation = text_nospace.strip(string.punctuation)
        for a in letters:
            if a in text_nopunctuation:
                per_letter_count = text_nopunctuation.count(a)
                letter_count = per_letter_count + letter_count
                #print(a, letter_count)
        
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
    print("---------------------------------")
    i = i + 1
    word_count = 0
    sentence_count = 0
    letter_count = 0
    average_word = 0.00