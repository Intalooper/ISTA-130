'''
John Diaz
Goal/Purpose - Master String and File I/O
'''

def US_to_EU(date):
    '''

    Purpose: Takes in a date in US format and returns the date in EU format
    Parameter (Type: String): Takes a string meant to represent a date
    Return: Returns the formatted string
    
    '''
    #the variable before holds a list of parts from the argument, namely, the day, month, and year
    parts = date.split('/')
    month = parts[0]
    day = parts[1]
    year = parts[2]

    eu_style = day + '.' + month + '.' + year
    return eu_style


def is_phone_num(number): 
    '''
    
     Purpose: Funciton takes in a number or string and evaluates whether or not it meets the expectations
              of the the function
     Parameter (Type: String): Takes a string meant to represent a number 
     Return: Returns True or False
    
    '''
    #breaks up the input into a list of strings 
    parts = number.split('-')
    if  len(parts) == 3 and parts[0].isdigit() and len(parts[0]) == 3 and parts[1].isdigit() and len(parts[1]) == 3 and parts[2].isdigit() and len(parts[2]) == 4:
        return True
    else:
        return False 


def redact_line(line):
    '''
    
    Purpose: Function takes in a number and converts all of the integers into X characters 
    Parameter (Type: String): The string is a list of numbers or a number 
    Return: Returns the edited string
     
    '''
    
    for i in range(len(line) - 12):
        if ((i == 0 or line[i - 1] == ' ') and line[i + 12] in ' \n' and is_phone_num(line[i:i + 12])):
            line = line[:i] + line[i:].replace(line[i:i + 12], "XXX-XXX-XXXX", 1)

    return line 


def redact_file(file_name):
    '''
    
    Purpose: Rewrites the given file with redacted numbers and a new file name. 
    Parameter (Type: String): Takes in the name of a .txt file.
    Returns: New file 

    '''
    input_f = open(file_name, 'r')
    input_file = file_name.split('.')
    output_file = input_file[0] + '_redacted' + '.' + input_file[1]
    fp = open(output_file, 'w')
    for i in input_f:
        fp.write(redact_line(i))
    input_f.close()
    fp.close()

def plagiarism(filename1, filename2):
    '''

    Purpose: Checks if any one line occurs in the same file 
    Parameters (Type: String): Takes in the names of two files
    Returns: True if two lines repeat and False if they don't

    '''
    file1 = open(filename1, 'r')
    for line1 in file1:
        file2 = open(filename2, 'r')
        for line2 in file2:
            if line1 == line2:
                file1.close()
                file2.close()
                return True
        file2.close()
        
    file1.close()
    file2.close()
    return False 

def count_word(filename, keyword):
    '''

    Purpose: Counts the number of times a keyword appears in a file 
    Parameters (Type: String): Takes in a file and keyword 
    Returns: Returns number of times the keyword appears in the file

    '''
    file = open(filename, 'r')
    keyword_count = 0 

    for line in file:
        keyword_count += line.count(keyword)
    
    return keyword_count

def redact_line(string_of_numbers):
    '''
    This function takes in a string and then replaces all of the valid numbers in the string with the following formatted string: XXX-XXX-XXXX
    '''
    #so what does this function need to do? It needs to take a string that has phone numbers and my job is to make the numbers into a bunch of xs. Now, what is the first thing that i need to do? Well i need the computer to know that it needs to traverse through teh string, and i Need it to know when it reaches a space, when it is at the begiinnion of the string or when it is at a new line character, hwoever, the new line character is something that is covered in its own condition. Now, we are goign to be traversing through index, and we are going to use the index for different reasons in the first part of the conditional statmente i ma checking whether i is 0 or if it is a space or a newline character, this is teh first condtiion taht needs to be checked in order for the fucntion to continue to keep moving forward. Now, what is the next fucnt? Well i need to know if the number that or the index that we're on is a number and what's more if it is an even number there is one more conditin that i need to check for. Waht is the condition? Well i know that it is a number at this point. I know where it begins, what else do i need to know? do i need to know how long it is? no, where it ends? maybe i can check if the end of the string is a space or something.hmmm i kso wehre was  was. Well 

    for i in range(len(string_of_numbers - 12)):
        if (i == 0 or string_of_numbers[i - 1] == ' ') and is_phone_num(string_of_numbers[i:i + 12]) and string_of_numbers[i + 12] in ' \n':
            line = line + string_of_numbers.replace(string_of_numbers[i:i + 12], 'XXX-XXX-XXXX', 1)
def main():
    print(US_to_EU('2/3/2024'))
    print(is_phone_num('123-456-78912'))
    print(redact_line(' 123-456-7890 333-232-23226 333-333-2323\n'))
    redact_file('redact_in.txt')
    print(plagiarism('highlight_in.txt', 'plagiarism_in.txt'))
    print(count_word('redact_in.txt', 'blah'))


if __name__ == '__main__':
    main()















































# '''
# Goal - to change the name of the orignal file when we make a new one
# '''
# def line_num(file):
#     '''
#     Parameters:
#         file: a file name as a string variable
#     '''
#     orginal_file = open(file, 'r')
#     #find index of '.' in our filneam
#     period_loc = file.find('.')

#     #add an extension based on where the period is (this code changes teh file name)
#     new_fname = file[:period_loc] + '_n' + file[period_loc:]

#     #write a new file with the same name but the string '_ln' added to the filename stem'
#     out_file = open(new_fname, 'w')

#     #creaete a line number per line to keep us on track

    
#     counter = 1
#     for line in orginal_file:
#         new_line = f'{counter}: {line}'
#         out_file.write(new_line)
#         counter += 1
#     # orginal_file.close()
#     # out_file.close()
#     # out_file.write(new_line)
#     return out_file

# def redact_line(string): 
#     new_string = ''
#     if is_phone_num(string[0:12]):
#         new_string += convert_to_x(string[0:12]) + ' '
#     if is_phone_num(string[13:25]):
#         new_string += convert_to_x(string[13:25]) + ' '
#     if is_phone_num(string[26:38]):
#         new_string += convert_to_x(string[26:38])
#     return new_string

# def redact_line2(string): 
#     numbers = ''
#     new_string = ''
#     trash_bin = ''
#     for ch in string:
#         if ch.isdigit() or ch == '-':
#             numbers += ch
#         else:
#             trash_bin += ch

#     new_string += convert_to_x(numbers[0:12]) + ' '
#     new_string += numbers[12:24] + ' '
#     new_string += convert_to_x(numbers[24:38])

#     return new_string
