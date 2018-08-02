class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, origion, friend_name, **kwargs):
        return cls(friend_name, origion.school, **kwargs)


class WorkingStudent(Student):
    '''
    The following syntax only works in Python3
    The super().__init(name, school) is how constructors are called in java
    '''
    def __init__(self,name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent("Anna", "Oxford", 200.00, "Devops")

#print(anna.marks)
#print(anna.job_title)
#print(anna.name)
#print(anna.salary)


### **kwargs stand for key word arguments.  We can never have normal args after kwargs. 
### Positional arguments are arguments where position of the argument is important.
### args, kwargs the position is not important

friend = WorkingStudent.friend(anna,"Greg",salary=50, job_title="developer")
'''
We need to add anna in order to create friend,  because as the method code shows, anna
holds information about the shool that Greg must have.
The order of the argument is also very important
'''
print(friend.name)
print(friend.school)
print(friend.salary)
print(friend.job_title)