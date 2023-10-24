
class Student:
    def __init__ (self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []
    
    # Dette er en metode
    def getFullName(self):
        return self.first_name + " " + self.last_name
    
    def getTotalCredits(self):
        totalCredits = 0
        for course in self.courses:
            totalCredits += course.credits
        return totalCredits

    def enroll_in_course(self, course):
        self.courses.append(course)

class Course:
    def __init__ (self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

# emil_berglund = Student("Emil", "Berglund", 19, 123456)
# Hans_Hansen = Student("Hans", "Hansen", 20, 654321)

#   print(f"{emil_berglund.first_name} {emil_berglund.last_name} er {emil_berglund.age} år gammel og har studentnummer {emil_berglund.student_id}")
#   print(f"{Hans_Hansen.first_name} {Hans_Hansen.last_name} er {Hans_Hansen.age} år gammel og har studentnummer {Hans_Hansen.student_id}")

#   print(emil_berglund.getFullName())
#   print(Hans_Hansen.getFullName())