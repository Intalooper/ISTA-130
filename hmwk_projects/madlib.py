'''
John Diaz
Class: Summer Mastery 
Date: July 27th

Purpose: This program is meant to take in a file and output specific information about the contents of the file. In addition, it creates a new file using anohter file, replacing its keywords with user input. 
'''
'''
Step 1: ask for input 
Step 2: replace the missing words with the input 
Step 3: traverse throught the file 
    I believe at this pooint i will have to identify some of the key terms and then replace thme with the user input 
    Here are the key terms: 
        1: NOUN 
        2: PLURAL NOUN
        3: VERB
        4: VERB PAST 
        5: ADJECTIVE 
Step 4: Create a new file and replace the old file with the new user input in place of the key terms
Step 5: Print a numerical analysis of the contents of the file 
'''
def print_report(file_name):
    '''
    Purpose: Reade the given file and print a report of the following information: 
        a. number of vowels 
        b. number of consanants 
        c. number of whitespaces 
        d. number of punctuation characters (not white space or not a letter)
        f. percent of the file composed of vowels, consanants, white spaces, and puncuation characters
        g. begin and end with a blank line
    '''
    new_file = open('personal.txt', 'w')
    argument_file = open(file_name, 'r')
    content = argument_file.read()
    #body of code below iterates by index through a file and checks for the amount of vowles in the strings. The following body of codes do the same thing for consonants, whitespace, and punctuation
    vowels = 0
    list_vowels = 'aeiouAEIOU'
    for i in range(len(content)):
        if content[i] in list_vowels:
            vowels += 1
    vowel_count = 'Vowels:'.ljust(20) + f'{vowels}'.rjust(5)

    consonants = 0
    list_consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for i in range(len(content)):
        if content[i] in list_consonants:
            consonants += 1
    consonant_count = f'Consonants:'.ljust(20) + f'{consonants}'.rjust(5)

    whitespace = 0
    list_whitespace= ' \n   '
    for i in range(len(content)):
        if content[i] in list_whitespace:
            whitespace += 1
    whitespace_count = 'Whitespace:'.ljust(20) + f'{whitespace}'.rjust(5)
    
    punctuation = 0
    punctuation_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" + ".,?!:;'\"/\\()[]{}...-_'’<>"
    for i in range(len(content)):
        if content[i] in punctuation_characters:
            punctuation += 1
    punctuation_count = 'Punctuation:'.ljust(20) + f'{punctuation}'.rjust(5)
    #Several calculations are performed below: total vowels, whitespace, consonants, and punctuation and the percentage of each. 
    total = vowels + consonants + whitespace + punctuation
    total_characters = 'Total:'.ljust(20) + f'{total}'.rjust(5)
    percent_vowels = f'Percent vowels:'.ljust(20) + f'{round(vowels/total * 100, 1)}'.rjust(5)
    percent_consonants = f'Percent consonants:'.ljust(20) + f'{round(consonants/total * 100, 1)}'.rjust(5)
    percent_whitespace = f'Percent spaces:'.ljust(20) + f'{round(whitespace/total * 100, 1)}'.rjust(5)
    percent_punctuation = f'Percent punctuation:'.ljust(20) +f'{round((punctuation/total * 100), 1)}'.rjust(5)
    
    last_line_formatting = '=' * 25
    line_for_formatting = '-' * 25
    print(f"\n-------{file_name}------\n{vowel_count}\n{consonant_count}\n{whitespace_count}\n{punctuation_count}\n{line_for_formatting}\n{total_characters}\n\n{percent_vowels}\n{percent_consonants}\n{percent_whitespace}\n{percent_punctuation}\n{last_line_formatting}")

def replace_parts_of_speech(line_from_file, part_of_speech):
    
    '''
    Purpose: Replaces any placeholders in a file line with the appropriate part of speech
    Parameters: 
        a) line_from_file (String): represents a line from a file that may contain part of speech labels 
        b) part_of_speech (String): indicates which part of speech label to replace with words
    '''
    counter = 0
    counter += line_from_file.count(part_of_speech)
    #for loop that replaces the x amount of the keyword with the input from the user
    for i in range(counter): 
        entry = input(f'Enter {part_of_speech.lower()}: ')
        line_from_file = line_from_file.replace(part_of_speech, entry, 1)
    return line_from_file
   
        
def complete_mad_lib(madlib_file):
    '''
    Purpose: Replaces all parts of speech labels in a file with words that are entered by the user onto a new file.
        personal note:
            you will need to use the replace parts of speech funciton and my guess is that i will have to run it fro every line in the function 
             rule to follow:
                You will need to replace the words in the following order: 
                    1.Plural Noun
                     2. Verb Past
                      3. Verb
                       4. Noun
                        5. Adjective 
    madlib_file (String): Takes in a file name
    '''
    #the following 4 lines creates the new file and opens the file that is passed in
    input_file = open(madlib_file, 'r')
    input_parts = madlib_file.split('.')
    output_file = 'MAD_' + input_parts[0] + '.' + input_parts[1] 
    output_open = open(output_file, 'w')
    #for loop that iterates thorugh each line in the file and replaces all of the keywords with whatever the user enters
        #Potential implementations: the code can be enhanced by telling the user when they didn't enter a word that aligns with the tyep of word that was asked for them. My understanding is that this would require a large language model or a very large list of dictionaries that aligns with every part of speech. 
    for line in input_file: 
        updated_line = replace_parts_of_speech(line, 'PLURAL NOUN')
        updated_line = replace_parts_of_speech(updated_line, 'VERB PAST')
        updated_line = replace_parts_of_speech(updated_line, 'VERB')
        updated_line = replace_parts_of_speech(updated_line, 'NOUN')
        updated_line = replace_parts_of_speech(updated_line, 'ADJECTIVE')
        output_open.write(updated_line)
    output_open.close()
    

def main():
    file_name = input('Enter file name: ')
    print_report(file_name)
    #print(replace_parts_of_speech('The NOUN VERB past the ADJECTIVE NOUN', 'NOUN'))
    complete_mad_lib(file_name)
if __name__ == '__main__':
    main()


#one hundred percent baby!

#Feedback for the code above
# Suggestions for Improvement:

# Expand Parameter Documentation: Be more descriptive about what each parameter does and expects. For instance, specify the expected format if there are any constraints on the input.
# Include Return Values: Document what each function returns, especially if it's not immediately obvious from the context.
# Error Handling: Mention how your code handles errors or unexpected inputs, which is crucial for developers to understand its robustness.
# Examples: Where applicable, include simple usage examples in the docstrings.
