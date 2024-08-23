class Student:
    '''
    blueprint for a digital student profile, which includes their name, id_number, gpa, phone, and email. 
    '''
    def __init__(self, name, id_number, gpa, phone, email):
        '''
        initializes each instance of student with several different strings to identify the unique student
        parameters:
            all are strings and are self-evident
        '''
        #all of the instance variables are strings
        self.name = name
        self.id_number = id_number
        self.gpa = gpa
        self.phone = phone 
        self.email = email 
    def __repr__(self):
        '''
        string representation for an object of student
        returns string instance_string
        '''
        instance_string = f'Name: {self.name}\n\nID: {self.id_number}\n\nGPA: {self.gpa}\n\nPhone Number: {self.phone}\n\nEmail: {self.email}'
        return instance_string
    
    def student_dict(self):
        '''
        Student metthod that creates a dictionary for the instance, where the name parameter is the key and the remaining values are the remaining parameters of the instance
        '''
        a_dict = {self.name: [self.id_number, self.gpa, self.phone, self.email]}
        
        return a_dict
    


def main():
    '''
    creates an instance of Students, prints the repr string and the instances student dictionary'''
    john = Student('John', '2839293', '4.0', '6232907937', 'johndiazleal@icloud.com')
    print(john)
    print(john.student_dict())
    

if __name__ == "__main__":
    main()