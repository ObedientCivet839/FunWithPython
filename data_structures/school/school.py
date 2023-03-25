### Primitive types

class Name:
    def __init__(self, first: str, middle: str, last: str):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.middle = middle.capitalize()
    
    def firstlast(self) -> str:
        # Format: https://docs.python.org/3/tutorial/inputoutput.html
        return '{first} {last}'.format(first=self.first, last=self.last)
    
    def fullname(self) -> str:
        """Returns fullname string with middle initial: Harry J. Potter"""
        return '{first} {middle}. {last}'.format(first=self.first, middle=self.middle[0], last=self.last)

    def __str__(self) -> str:
        return self.fullname()

from datetime import date

class Profile:
    def __init__(self, name: Name, dob: str):
        self.name = name
        self.dob = date.fromisoformat(dob)

    def __str__(self) -> str:
        return '{name: <15} - DOB: {dob} - Age: {age}'.format(name=self.name.fullname(), dob=self.dob.isoformat(), age=self.age)
    
    @property
    def age(self):
        gap = date.today() - self.dob
        return gap.days // 365

class Person:
    def __init__(self, profile: Profile):
        self._profile = profile

### - END Primitive types

class School:
    classrooms = []
    grades = []
    students = []
    employees = []

    def __init__(self, name: str):
        self._name = name
        self._students = []
    
    def __str__(self) -> str:
        return self._name

class Student(Person):
    numStudents = 0

    # constructor
    def __init__(self, profile: Profile):
        Profile.__init__(self, profile)

        # Classes that this student takes
        self._student_id = 0
        self.classes = list[Class]
        self.grades = list[ReportCard]

    @property
    def grade(self):
        return self.age - 6

    def enroll(self, school: School) -> int:
        self._school = school
        self._school._students.append()
        return len(self._students)

    def enroll_class(self, cls):
        self.classes.append(cls)
    
    def attend_class(self, cls):
        pass

    def __str__(self) -> str:
        return '{name} - Grade: {grade} - School: {school}'.format(name=self._profile, grade=self.grade, school=self.school)

class Employee:
    pass

class Teacher:
    pass

class Principal:
    pass


class ReportCard:
    pass


class SchoolGrade:
    numStudents = 0

class Schedule:
    def __init__(self, dow = 0, time = 0):
        pass

class Subject:
    # multiple classes
    pass

class Class:
    def __init__(self, name = "", grade = 0):
        self.name = name
        self.grade = grade
        self.schedule = Schedule()
        self.teacher = None

class Classroom:
    
    pass


if __name__ == '__main__':
    p1 = Profile(Name("John", "Hey" "Smith"), '1203-02-23')
    sc = School("Berkeley")
    s1 = Student(p1, sc)
    print(s1)
    
