#creating a parent class called Students
class Students:
    def __init__(self, first_name, last_name, student = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@gmail.com'
    #print("check")

#creating instance of the parent class
student_1 = Students("Kehinde", "Orolade")
student_2 = Students("Abubakar", "Sadiq")
print(student_2.last_name)

#creating the child class group leader
class group_leader(Students):
    def __init__(self, first_name, last_name, student=[]):
        super().__init__(first_name, last_name)
        self.student = student

    #check
    #print("child class has been created")


#defining a method that adds students to the list of student under the group leader
    def add_students(self, student):
        self.student.append(student)
        print(self.student, student)
    #print("method created successfully")

#defining a method that removes student from the list of students under the group leader
    def remove(self, student):
        self.student.remove(student)
        print(self.student, student)
    #check
    #print("item removed successfully")

#defining a method that prints out the full names of students in the list of students under group leader
    def fullname(self):
        '{} {}'.format(self.first_name, self.last_name)
        return '{} {}'.format(self.first_name, self.last_name)
    #check
    #print("Successful")

#creating 3 more instances of the parent class
student_3 = Students("Joyce",  "Ezeonwu")
student_4 = Students("Idowu",  "Adesanya")
print(student_4.first_name)

#creating 2 instances of the sub class
follower_1 = group_leader("Gideon", "Oko")
follower_2 = group_leader("Tosin", "Ajao")
print(follower_2.last_name)



#adding 2 students each to the list of students under the instance of subclass
# follower_1.add_students("Akawi")
# follower_1.add_students("Courage")
# follower_2.add_students("Ifeanyi")
# follower_2.add_students("Idemili")

#remove 1 student each from the list of students under the instances of subclass
# follower_1.remove("Courage")
# follower_2.remove("Ifeanyi")

#print the full name of the students in the list of students under the instances of subclass
print(follower_1.fullname())
print(follower_2.fullname())

#print the email of the instances of subclass
def email(self, first_name, last_name):
    self.email = first_name + '.' + last_name + 'gmail.com'
print(follower_1.email)
print(follower_2.email)