# class student
class Student:
    def __init__(self, id, name, math, literature, chemistry):
        self.id = id
        self.name = name
        self.math = math
        self.literature = literature
        self.chemistry = chemistry

    def calculateAvg(self):
        return (self.math + self.literature + self.chemistry) / 3
    
    def printInfo(self):
        print(f"id: {self.id} - name: {self.name} - math: {self.math} - literature: {self.literature} - chemistry: {self.chemistry}")
    
# class student manager
class StudentManager:
    def __init__(self):
        self.studentList:list[Student] = []
    
    def addStudent(self, student:Student):
        self.studentList.append(student)

    def printMoreThan5(self):
        for student in self.studentList:
            avg = student.calculateAvg()
            if avg > 5:
                student.printInfo()

    def chemistryBelow5(self):
        for student in self.studentList:
            if student.chemistry < 5:
                student.printInfo()


# test
student1 = Student(1, "An", 3, 7, 5)
student2 = Student(2, "Viet", 5, 6, 4)
student3 = Student(3, "Nguyen", 8, 3, 5)
student4 = Student(4, "Jackie", 9, 10, 10)
student5 = Student(5, "Charlie", 5, 3, 3)

student_manager = StudentManager()

student_manager.addStudent(student1)
student_manager.addStudent(student2)
student_manager.addStudent(student3)
student_manager.addStudent(student4)
student_manager.addStudent(student5)

print("Students average above 5: ")
student_manager.printMoreThan5()
print("Students that have chemistry below 5: ")
student_manager.chemistryBelow5()