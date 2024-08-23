'''
Name: John Diaz-Leal
Class: ISTA 130
Professor: Dozal

Purpose: 
'''

#Do not use the tab character for indentation 
#keep in mind good nameing practices, and use loops where there is duplicated code
#document!

#3 values: name - body weight kg - brain g
#First task: collect the itmes into listss
#Functionalities to add: allow the user to add an animal and remove one or view information associated with the animal 
#Once the program is done and the user has inputted everytying that he wants, the program will converst all of the 

def find_insert_position(mammal, list_of_strings): 
    '''
    Purpose: Returnds an integer indicating the positon (index) in the list of names such that if you inserted the given mammal's name inot the list at that index the list would still be in alphabetical order. 
    Parameters:
        mammal (String): Terrestrial mammal name
        list_of_strings (String): List of strings in alphabetical order
    Returns (int): Returns the index of the mammal in the list of strings that is in alphabetical order
    
    '''
    index_for_mammal = 0 
    for index, animal in enumerate(list_of_strings): 
        if mammal > animal:
            index_for_mammal = index + 1
        else:
            index_for_mammal = index
            return index_for_mammal
    return index_for_mammal
        #okay suppose that we reach a point where the animla that we have is not greateer than animal, but that's because we are at the end of the string, would we even get to that point? No, i think the loop will go up until the last element in the list, and make the comparison, and the final comparison will be made and either mammal will be greater or not, and at this point the loop will exit and i will have to return the index for the mmam

def populate_lists(mammal_list, mammal_weights, brain_weights):
    '''
    Purpose: Makes three independent lists holding unique values about one property of an animals (Name, body weight, and brain weight)
    Parameters: 
        a) Mammal_list (Type: Strings): Contains a list of animal names
        b) Mammal_Body_Weights (Type: Floats): Holds a list of animal body weights
        c) Brain_weights (Type: Floats): Holds a list of brain weights
    '''

    open_file = open('BrainBodyWeightKilos.csv', 'r')
    
    for line in open_file:
        parts = line.split(',')
        mammal_list.append(parts[0].title())
        mammal_weights.append(float(parts[1]))
        brain_weights.append(float(parts[2]))


def write_converted_csv(file, list_mammals, mammal_weights, brain_weights):
    '''
    Purpose: Writes a new formatted .csv file with the given file name where the unit for weight is pounds and names are in title case
        Condition: Floats written to the file should be rounded 2 decimal places
    Parameters:
        file (Type: String): Takes in a new file name
        list_mammals (Type: List): Takes in a list of strings 
        mammal_weights (Type: List): Takes in a list of floats
        brain_weights (Type: List): Takes in a list of floats 
        
    ''' 
    new_file = open(file, 'w')

    for i in range(len(mammal_weights)):
        weight_lb = mammal_weights[i] * 2.205
        mammal_weights[i] = weight_lb
    for i in range(len(brain_weights)):
        weight_lb2 = brain_weights[i] * 0.0022
        brain_weights[i] = weight_lb2
  
    for i in range(len(list_mammals)):
        new_file.write(f'{list_mammals[i].title()},{str(round(mammal_weights[i], 2))},{str(round(brain_weights[i], 2))}\n')
    
    new_file.close()
    
def main():
    mammal_names = []
    body_weights = []
    brain_weights = []
    populate_lists(mammal_names, body_weights, brain_weights)
    while True:
        user_response = input('\nEnter animal name (or "q" to quit): ').title()
        #prompts user to add new animal data to file
        if user_response == 'Q':
            write_converted_csv('BrainBodyWeightPounds.csv', mammal_names, body_weights, brain_weights)
            return 
        elif user_response not in mammal_names:
            print(f'File does not contain "{user_response}".')
            user_response2 = input(f'Add "{user_response}" to file? (y|n) ')
            if user_response2 == 'y':
                #if the user says yes to this then i hae to add all of the itmes to all of the lists
                new_body_weight = float(input(f'Enter body weight for "{user_response}" in kilograms: ')) 
                new_brain_weight = float(input(f'Enter brain weight for "{user_response}" in grams: ')) 
                new_animal_index = find_insert_position(user_response, mammal_names)
                mammal_names.insert(new_animal_index, user_response)
                body_weights.insert(new_animal_index, round(new_body_weight, 2))
                brain_weights.insert(new_animal_index, round(new_brain_weight, 2))
            else:
                continue
        elif user_response in mammal_names:
            input_index = mammal_names.index(user_response)
            print(f'{user_response}: body = {body_weights[input_index]}, brain = {brain_weights[input_index]}')
            delete_input = input(f'Delete "{user_response}"? (y|n)')
            if delete_input == 'y':
                del mammal_names[input_index]
                del body_weights[input_index]
                del brain_weights[input_index]
            else:
                continue 
        else:
            continue 


   


if __name__ == '__main__':
    main()
