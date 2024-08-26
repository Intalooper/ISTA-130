'''
John Diaz
Class: ISTA 130
Professor: Dozal
Start Date: N/A
Finish Date: N/A
'''

class Student:
    '''
    blueprint for a digital student profile, which includes their name, id_number, gpa, phone, and email 
    '''
    def __init__(self, name, id_number, gpa, phone, email):
        '''
        Initializes each instance of student with several different strings to identify the unique student
        Parameters (Type: String):
            all are strings and are self-evident
        Returns None
        '''
        #all of the instance variables are strings
        self.name = name
        self.id_number = id_number
        self.gpa = gpa
        self.phone = phone 
        self.email = email 
    def __repr__(self):
        '''
        String representation for an object of Student
        Returns: returns 'instance_string' -> (Type: String)
        '''
        instance_string = f'Name: {self.name}\n\nID: {self.id_number}\n\nGPA: {self.gpa}\n\nPhone Number: {self.phone}\n\nEmail: {self.email}'
        return instance_string
    
    def student_dict(self):
        '''
        Class method creates a dictionary for the istance, where the name instance variable is the key and the remaining values are the remaining instance variables
        Returns: returns dictionary (Type: Dic)
        '''
        a_dict = {self.name: [self.id_number, self.gpa, self.phone, self.email]}
        
        return a_dict
    


def main():
    '''
    Creates an instance of Students, prints the repr string and the instances student dictionary
    '''
    john = Student('John', '2839293', '4.0', '6232907937', 'johndiazleal@icloud.com')
    print(john)
    print(john.student_dict())
    

if __name__ == "__main__":
    main()
