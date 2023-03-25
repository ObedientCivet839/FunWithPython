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

def createProfile(first: str, middle: str, last: str, dob: str) -> Profile:
    full_name = Name(first, middle, last)
    profile = Profile(full_name, dob)
    return profile