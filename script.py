class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    

class Student(Person):
    def __init__(self , name , age , grade_level):
        super().__init__(name , age)
        self.grade_level = grade_level
        self.grades = []

    # add a grade
    def add_grade(self , grade):
        self.grades.append(grade)
    
    # Calculate grade average
    def calculate_grade_average(self):
        if not self.grades:
            return "No grades available"

        return sum(self.grades) / len(self.grades)
        
    # Introduce student
    def introduce(self):
        ret = super().introduce()
        ret += "I am a student."
        return ret
        
class Teacher(Person):
    def __init__(self, name , age , subject_taught):
        super().__init__(name , age)
        self.subject_taught = subject_taught

    def introduce(self):
        ret = super().introduce()
        ret += "I am a teacher."
        return ret

class Class:
    def __init__(self, name , students=[] , teacher = None):
        self.name = name
        self.students = students
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self , student):
        self.students.remove(student)

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_class_info(self):
        class_info = f"Class: {self.name}\n"
        class_info += f"Teacher: {self.teacher.name}\n"
        class_info += "Students: \n"
        for student in self.students:
            class_info += f"- {student.name}, grade {student.grade_level}, Average Grade: {student.calculate_grade_average()}\n"
        return class_info

student_1 = Student("John" , 25 , 5)
student_2 = Student("Mike" , 26 , 5)
student_3 = Student("Selma" , 30 , 5)
student_4 = Student("Narmine" , 21 , 5)
teacher_1 = Teacher("Alaa" , 99 , "Math")
teacher_2 = Teacher("Yaya" , 41 , "Math")
teacher_3 = Teacher("Saif" , 30 , "Math")
teacher_4 = Teacher("Wael" , 42 , "Math")

students_and_teachers = [student_1 , student_2 , teacher_1 , student_3 , teacher_2 , teacher_3 , student_4 , teacher_4]
class_1 = Class("Web Development" , teacher=teacher_1)
class_1.add_student(student_1)
class_1.add_student(student_2)
class_1.add_student(student_3)
class_1.add_student(student_4)

student_1.add_grade(15)
student_1.add_grade(18)
student_1.add_grade(16)

student_2.add_grade(10)
student_2.add_grade(20)
student_2.add_grade(12.5)

print(class_1.get_class_info())
# for person in students_and_teachers:
#     print(person.introduce())

