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
        """Returns fullname string with middle initial: Trevor T. Ta """
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

def printPeople():
    p = Profile(Name("Trieu", "Huy", "Ta"), '1966-09-19')
    print(p)
    p = Profile(Name("Hien", "Duc", "Nguyen"), '1966-03-15')
    print(p)
    p = Profile(Name("trevor", "triet", "Ta"), '1991-08-13')
    print(p)
    p = Profile(Name("Thuyet", "Hien", "Ta"), '1998-06-06')
    print(p)

if __name__ == '__main__':
    p1 = Profile(Name("trevor", "triet", "Ta"), '1991-08-13')
    p2 = Profile(Name("Thuyet", "Hien", "Ta"), '1998-06-06')
    sc = School("Berkeley")
    s1 = Student(p1, sc)
    print(s1)
    s2 = Student(p2, sc)
    print(s2)
    print(sc.students)
    
